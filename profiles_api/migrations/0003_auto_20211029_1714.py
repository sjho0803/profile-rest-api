# Generated by Django 2.2 on 2021-10-29 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='user_profile_id',
            new_name='user_profile',
        ),
    ]
