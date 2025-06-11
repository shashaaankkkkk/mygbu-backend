from django.contrib import admin
from .models import User , UserRole , Document , SystemLog


# Register your models here.
admin.site.register([User , UserRole , Document , SystemLog])
