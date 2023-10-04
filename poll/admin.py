from django.contrib import admin
from poll.models import UserProfileInfo,Question,Choice,Patient
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Patient)
