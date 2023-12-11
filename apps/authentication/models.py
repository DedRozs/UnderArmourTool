# -*- encoding: utf-8 -*-

from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserType(models.TextChoices):
    ADMIN = "Admin"
    USER = "User"
    EVENT_PROVIDER = "Event Provider"
    TEST_USER = "Testing"

class Features(models.TextChoices):
    EDIT = "Edit User"
    EMAIL = "Email"
    DOB = "DOB"
    ACCOUNTTYPE = "Account Type"
    PARENTID = "Parent ID"
    EVENTCLAIMINQ ="Event Claim Inquiry"

class Partner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, default=None)

    def __str__(self):
        return self.name

class Permission(models.Model):
    feature = models.CharField(max_length = 100, choices=Features.choices)
    allowed = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.feature} - {self.user.username}"

    class Meta:
        db_table = "Permissions"

class UserProfile(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField( max_length=20 ,default="User")
    partner = models.ManyToManyField(Partner, default=None, blank=True, related_name="allowed_partners")
    
    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "UserProfiles"