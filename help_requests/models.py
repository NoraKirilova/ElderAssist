from django.db import models
from django.contrib.auth.models import User


class HelpRequest(models.Model):
    CATEGORY_CHOICES = [
        ("shopping", "Пазаруване"),
        ("medicine", "Доставка на лекарства"),
        ("transport", "Транспорт"),
        ("company", "Социална активност"),
        ("other", "Друго"),
    ]

    STATUS_CHOICES = [
        ("open", "Отворена"),
        ("assigned", "Има одобрен кандидат"),
        ("closed", "Затворена"),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="help_requests")

    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)

    start_location = models.CharField(max_length=200, blank=True)
    end_location = models.CharField(max_length=200, blank=True)

    is_paid = models.BooleanField(default=False)
    payment_note = models.CharField(max_length=200, blank=True)

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="open")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = [
        ("pending", "Изчакваща"),
        ("accepted", "Приета"),
        ("rejected", "Отхвърлена"),
    ]

    help_request = models.ForeignKey( HelpRequest, on_delete=models.CASCADE, related_name="applications")

    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")

    message = models.TextField(blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("help_request", "applicant")

    def __str__(self):
        return f"{self.applicant.username} -> {self.help_request.title}"
    
