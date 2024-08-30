from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model
from django.utils import timezone

# Custom User Model
class CustomUser(AbstractUser):
    ADMIN = 'Admin'
    USER = 'User'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions_set', blank=True)

    def __str__(self):
        return f'{self.username} ({self.role})'

# Base Model
class Base(models.Model):
    status = models.BooleanField(default=1)
    activity_code = models.IntegerField(default=1)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} ({self.pk})"

# UserProfile Model
class UserProfile(Base):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# UserRole Model
class UserRole(Base):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.role_name}"

# Privileges Model
class Privileges(Base):
    privilege_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.privilege_name

# Roles Model
class Roles(Base):
    role_name = models.CharField(max_length=100, blank=True, null=True)
    privileges = models.ManyToManyField(Privileges)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.role_name
