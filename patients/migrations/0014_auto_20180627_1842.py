# Generated by Django 2.0.2 on 2018-06-27 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0013_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='ethnicity',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='initial',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='insurance',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='state',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
