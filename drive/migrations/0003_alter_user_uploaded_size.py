# Generated by Django 4.0.1 on 2022-01-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uploaded_size',
            field=models.IntegerField(default='0'),
        ),
    ]
