from django.contrib import admin

# Register your models here.

from .models import User,Server,Alert

admin.site.register((User,Server,Alert))