from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = [
        ("male", "Мъж"),
        ("female", "Жена"),
        ("other", "Друго"),
        ("prefer_not_to_say", "Предпочитам да не казвам"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    full_name = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100, help_text="Квартал в София")
    phone_number = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, blank=True)

    interests = models.TextField(blank=True)
    needs = models.TextField(blank=True)

    def __str__(self):
        return self.full_name or self.user.username
