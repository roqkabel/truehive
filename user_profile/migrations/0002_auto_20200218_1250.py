# Generated by Django 2.2.8 on 2020-02-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='account_type',
            field=models.CharField(choices=[('FL', 'Freelancer'), ('CL', 'Client')], max_length=2),
        ),
    ]
