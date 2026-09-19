from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User


@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    role = request.data.get('role')
    email = request.data.get('email')  # can be None

    if not username or not password or not role:
        return Response(
            {"error": "username, password and role are required"},
            status=400
        )

    role = role.lower()
    if role not in ["doctor", "patient", "admin"]:
        return Response(
            {"error": "Invalid role"},
            status=400
        )

    # Create user; email can be None/empty now
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email or ""
    )
    user.role = role
    user.save()

    return Response({"msg": "User created"})


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {"error": "username and password are required"},
            status=400
        )

    user = authenticate(username=username, password=password)

    if user:
        return Response({
            "user_id": user.id,
            "role": user.role,
            "email": user.email
        })

    return Response(
        {"error": "Invalid credentials"},
        status=400
    )
