from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User

@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    role = request.data.get('role')
    email = request.data.get('email')

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )
    user.role = role.lower()
    user.save()

    return Response({"msg": "User created"})


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        return Response({
            "user_id": user.id,
            "role": user.role,
            "email": user.email
        })

    return Response({"error": "Invalid credentials"}, status=400)