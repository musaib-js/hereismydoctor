# Generated by Django 4.1.6 on 2023-02-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0007_doctor_duty_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='duty_day',
            field=models.CharField(default='Please enter the data here', max_length=500),
        ),
    ]