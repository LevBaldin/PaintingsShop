from django.contrib import admin

# Register your models here.
from .models import Picture, About

admin.site.register(Picture)
admin.site.register(About)