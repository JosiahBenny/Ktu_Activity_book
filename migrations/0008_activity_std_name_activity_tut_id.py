# Generated by Django 5.0.3 on 2024-04-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_student_info_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='std_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='tut_id',
            field=models.IntegerField(default=0),
        ),
    ]
