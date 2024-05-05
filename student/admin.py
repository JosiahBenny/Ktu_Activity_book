from django.contrib import admin
from . import models

class display1(admin.ModelAdmin):
    list_display=('regno','name','semester')

class display2(admin.ModelAdmin):
    list_display=('username',)

class display3(admin.ModelAdmin):
    list_display=('act_name','act_points','std_id')

admin.site.register(models.student_info,display1)
admin.site.register(models.stud_login,display2)
admin.site.register(models.activity,display3)
