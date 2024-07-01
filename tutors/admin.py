from django.contrib import admin
from .models import tutors_info,tutors_login

class tutdisplay1(admin.ModelAdmin):
    list_display=('tut_id','name')
class tutdisplay2(admin.ModelAdmin):
    list_display=('username',)
admin.site.register(tutors_info,tutdisplay1)
admin.site.register(tutors_login,tutdisplay2)