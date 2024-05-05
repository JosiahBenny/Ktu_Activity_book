from django.db import models

class student_info(models.Model):
    regno=models.IntegerField(primary_key=True,null=False)
    name=models.CharField(max_length=30)
    tut_id=models.IntegerField(null=False)
    total_points=models.IntegerField(default=0)
    semester=models.IntegerField(default=1)


class activity(models.Model):
    act_name=models.CharField(max_length=30)
    act_points=models.IntegerField(default=0)
    status=models.CharField(max_length=1) #expected values are 0 (new not marked),1(accepted and marks)& 2(rejected not marked)
    std_id=models.ForeignKey(to=student_info,to_field='regno',on_delete=models.CASCADE)
    proof=models.FileField(upload_to="josiah",null=True)
    std_name=models.CharField(max_length=30,null=True)
    tut_id=models.IntegerField(null=True)

class stud_login(models.Model):
    username=models.IntegerField(primary_key=True)
    password=models.CharField(max_length=20)
