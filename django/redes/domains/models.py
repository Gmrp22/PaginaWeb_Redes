from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class domainUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    domain = models.TextField(max_length=10, blank=False)
    desciprion = models.TextField(blank=True)
    domain_user = models.TextField(max_length=8, blank=False)
    passwrd = models.TextField(max_length=10)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain
