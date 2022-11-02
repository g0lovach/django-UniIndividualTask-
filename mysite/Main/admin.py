from django.contrib import admin
from .models import Firms, Types, Technic

# Register your models here.

admin.site.register(Firms)
admin.site.register(Types)
admin.site.register(Technic)