# Generated by Django 2.0.7 on 2019-07-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0016_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_dictionary',
            field=models.TextField(default=''),
        ),
    ]
