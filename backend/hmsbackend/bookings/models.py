from django.db import models
from hmsbackend.accounts.models import User

class AvailabilitySlot(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)


class Booking(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    slot = models.ForeignKey(AvailabilitySlot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
