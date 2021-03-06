# Generated by Django 2.0.2 on 2018-06-24 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_auto_20180624_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='allergies',
            field=models.BooleanField(default=False, verbose_name='Ask about Allergies'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='initialized',
            field=models.BooleanField(default=False, verbose_name='Initial Visit'),
        ),
    ]
