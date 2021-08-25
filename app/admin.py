from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from app.models import DBFeedback

admin.site.register(DBFeedback)