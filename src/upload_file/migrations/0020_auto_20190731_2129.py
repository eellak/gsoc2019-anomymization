# Generated by Django 2.0.7 on 2019-07-31 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0019_auto_20190731_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='change_in_user_dictionary_since_last_update',
        ),
        migrations.AddField(
            model_name='document',
            name='copy_of_user_dictionary',
            field=models.TextField(default=''),
        ),
    ]
