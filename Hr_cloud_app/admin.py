from django.contrib import admin

from Hr_cloud_app import models
from Hr_cloud_app.views import hr

# Register your models here.
admin.site.register(models.Login)
admin.site.register(hr)