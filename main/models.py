from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True)
    # Add this line below:
    date_of_birth = models.DateField(null=True, blank=True)


class Plan(models.Model):
    class STATUS(models.TextChoices):
        todo = 'TODO', 'TODO'
        in_progress = 'In Progress', 'In Progress'
        completes = 'Completed', 'completed'
    title = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS.choices, default=STATUS.todo)
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

