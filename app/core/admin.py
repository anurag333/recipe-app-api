from django.contrib import admin
from core import models

# Register your models here.

# added this line extra for making the error goawasy
admin.site.register(models.User)
