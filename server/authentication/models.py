from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    USERNAME_FIELD = 'email' # Iniciar sesión con el correo, no con el username.
    REQUIRED_FIELDS = ['username', 'password'] # Campos requeridos para crear un usuario.
