# Generated by Django 4.0.1 on 2022-01-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0004_alter_file_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]