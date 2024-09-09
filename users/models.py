import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    MALE_SEX = 1
    FEMALE_SEX = 2
    SEX_CHOICES = (
        (MALE_SEX, 'male'),
        (FEMALE_SEX, 'female')
    )

    first_name = models.CharField(max_length=150, db_index=True, blank=True)
    last_name = models.CharField(max_length=150, db_index=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    sex = models.PositiveSmallIntegerField(choices=SEX_CHOICES, null=True, blank=True)

    @staticmethod
    def generate_username():
        return uuid.uuid4().hex.upper()
