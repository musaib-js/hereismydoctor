# Generated by Django 4.1.6 on 2023-02-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='hospital',
            field=models.ManyToManyField(related_name='hospital', to='hospitals.hospital'),
        ),
    ]
