from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register your models here.
@admin.register(get_user_model()) # Crear, editar y boorar usuarios.
class CustomUserAdmin(UserAdmin):
    pass

admin.site.unregister(Group) # Deshabilita los grupos (no se van a usar).
