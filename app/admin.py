from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from app.models import DBFeedback, DBLinkAll, DBProject, DBApis

admin.site.register(DBFeedback)
admin.site.register(DBLinkAll)
admin.site.register(DBProject)
admin.site.register(DBApis)