from django.contrib import admin

from Hr_cloud_app import models
from Hr_cloud_app.models import Employee, Work, Hr, Complaint, Reply

admin.site.register(models.Login)
admin.site.register(Hr)
admin.site.register(Employee)
admin.site.register(Work)
admin.site.register(Complaint)
admin.site.register(Reply)