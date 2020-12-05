from django.contrib import admin
from .models import Highlight, Schedule, Schedule2, Schedule3, User_Data, Inquiry
# Register your models here.
admin.site.register(Schedule)
admin.site.register(Schedule2)
admin.site.register(Schedule3)
admin.site.register(Highlight)
admin.site.register(User_Data)
admin.site.register(Inquiry)