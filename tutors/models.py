from django.db import models

class tutors_info(models.Model):
    name=models.CharField(max_length=30)
    tut_id=models.IntegerField(primary_key=True)
    total_stud=models.IntegerField(default=0)

class tutors_login(models.Model):
    username=models.IntegerField(primary_key=True)
    password=models.CharField(max_length=20)
    
