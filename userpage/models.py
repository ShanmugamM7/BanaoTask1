from django.contrib.auth.models import AbstractUser
from django.db import models

class UserDetails(AbstractUser):
    USER_TYPE_CHOICES = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='Not Mentioned')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )