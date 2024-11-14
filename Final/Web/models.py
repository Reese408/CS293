from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_user_permissions(self, obj=None):
        return Permission.objects.filter(user=self)

    def get_group_permissions(self, obj=None):
        return Permission.objects.filter(group__user=self)
    
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class QuoteRequest(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('Pool Construction', 'Pool Construction'),
        ('Liner Install/Replacement', 'Liner Install/Replacement'),
        ('Home Renovation', 'Home Renovation'),
        ('Landscape Design', 'Landscape Design'),
        ('General Construction', 'General Construction'),
        ('Other', 'Other'),
    ]
    
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='quote_requests')

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES)
    location = models.CharField(max_length=255)
    details = models.TextField()
    
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Quote Request from {self.name} for {self.project_type} in {self.location}"

