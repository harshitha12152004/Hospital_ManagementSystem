from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AvailabilitySlot, Booking
from accounts.models import User
from django.core.mail import send_mail
from .google_calendar import create_event

@api_view(['POST'])
def create_slot(request):
    AvailabilitySlot.objects.create(
        doctor_id=request.data.get('doctor_id'),
        date=request.data.get('date'),
        start_time=request.data.get('start_time'),
        end_time=request.data.get('end_time')
    )
    return Response({'message': 'Slot created'})


@api_view(['GET'])
def get_slots(request):
    slots = AvailabilitySlot.objects.filter(is_booked=False)
    return Response(list(slots.values()))


@api_view(['POST'])
def book_slot(request):
    try:
        with transaction.atomic():
            slot = AvailabilitySlot.objects.get(id=request.data.get('slot_id'))

            if slot.is_booked:
                return Response({'error': 'Already booked'})

            patient = User.objects.get(id=request.data.get('patient_id'))
            doctor = slot.doctor

            Booking.objects.create(
                patient=patient,
                doctor=doctor,
                slot=slot
            )

            slot.is_booked = True
            slot.save()

            # 📧 EMAIL TO PATIENT
            if patient.email:
                send_mail(
                    "Appointment Confirmation",
                    f"Dear {patient.username}, your appointment with Dr. {doctor.username} on {slot.date} at {slot.start_time} is confirmed.",
                    None,
                    [patient.email],
                    fail_silently=False,
                )

            # 📧 EMAIL TO DOCTOR
            if doctor.email:
                send_mail(
                    "New Appointment",
                    f"Dr. {doctor.username}, new booking by {patient.username} on {slot.date} at {slot.start_time}.",
                    None,
                    [doctor.email],
                    fail_silently=False,
                )
            try:
                create_event(slot, patient, doctor)
            except Exception as e:
                print("calender error:",e)
        return Response({'msg': 'Booked successfully'})

    except Exception as e:
        print(e)
        return Response({'error': 'booking failed'})