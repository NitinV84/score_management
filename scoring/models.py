from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    """
    Custom user manager to handle user creation.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user.
        """
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a new superuser.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    """
    Custom user model.
    """
    class UserRoles(models.TextChoices):
        Admin = "AD"
        Judges = "JD"
        Staff = "ST"
        EscaleStaff = "ES"
        Users = "US"

    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
        
    userrole = models.CharField(
        choices=UserRoles.choices,
        max_length=20,
        default=UserRoles.Users
    )
    objects = UserManager()

class Category(models.Model):
    """
    Model representing a category.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Application(models.Model):
    """
    Model representing an application.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default="pending")
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s application for {self.category.name} ({self.status})"
