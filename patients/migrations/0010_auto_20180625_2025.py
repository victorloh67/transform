# Generated by Django 2.0.2 on 2018-06-26 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0009_auto_20180625_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initial',
            name='bmi',
            field=models.FloatField(verbose_name='BMI'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='bp_diastolic_lie',
            field=models.PositiveIntegerField(help_text='Enter Diastolic BP while lying down', verbose_name='BP Diastolic - Lying Down'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='bp_diastolic_sit',
            field=models.PositiveIntegerField(help_text='Enter Diastolic BP while sitting', verbose_name='BP Diastolic - Sitting'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='bp_diastolic_stand',
            field=models.PositiveIntegerField(help_text='Enter Diastolic BP while standing', verbose_name='BP Diastolic - Standing'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='bp_systolic_lie',
            field=models.PositiveIntegerField(help_text='Enter Systolic BP while lying down', verbose_name='BP Systolic - Lying Down'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='bp_systolic_sit',
            field=models.PositiveIntegerField(help_text='Enter Systolic BP while sitting', verbose_name='BP Systolic - Sitting'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='bp_systolic_stand',
            field=models.PositiveIntegerField(help_text='Enter Systolic BP while standing', verbose_name='BP Systolic - Standing'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='date_initial',
            field=models.DateField(verbose_name='Date of Initial Visit'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='hr_lie',
            field=models.PositiveIntegerField(help_text='Enter Heart rate while lying down', verbose_name='Pulse - Lying Down'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='hr_sit',
            field=models.PositiveIntegerField(help_text='Enter Heart rate while sitting', verbose_name='Pulse - Sitting'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='hr_stand',
            field=models.PositiveIntegerField(help_text='Enter Heart rate while sitting', verbose_name='Pulse - Standing'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='o2_lie',
            field=models.PositiveIntegerField(help_text='Enter O2 while lying down', verbose_name='O2 - Lying Down'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='o2_sit',
            field=models.PositiveIntegerField(help_text='Enter O2 while sitting', verbose_name='O2 - Sitting'),
        ),
        migrations.AlterField(
            model_name='initial',
            name='o2_stand',
            field=models.PositiveIntegerField(help_text='Enter O2 while sitting', verbose_name='O2 - Standing'),
        ),
    ]
