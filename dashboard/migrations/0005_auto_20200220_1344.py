# Generated by Django 2.2.8 on 2020-02-20 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200220_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.DateField(),
        ),
    ]
