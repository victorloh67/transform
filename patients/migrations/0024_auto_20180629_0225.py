# Generated by Django 2.0.2 on 2018-06-29 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0023_auto_20180628_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allergy',
            name='allergen',
        ),
        migrations.AddField(
            model_name='allergy',
            name='allergen',
            field=models.ForeignKey(help_text='Select an Allergen for this patient', null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.Allergen', verbose_name='Select Allergen'),
        ),
        migrations.RemoveField(
            model_name='diagnose',
            name='illness',
        ),
        migrations.AddField(
            model_name='diagnose',
            name='illness',
            field=models.ForeignKey(help_text='Select an illness for this patient', null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.Illness', verbose_name='Select Illness'),
        ),
        migrations.RemoveField(
            model_name='info',
            name='insurance',
        ),
        migrations.AddField(
            model_name='info',
            name='insurance',
            field=models.ForeignKey(help_text='Select an insurance for this patient', null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.Insurance'),
        ),
        migrations.RemoveField(
            model_name='initial',
            name='referrer',
        ),
        migrations.AddField(
            model_name='initial',
            name='referrer',
            field=models.ForeignKey(help_text='Select a referrer for this patient', null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.Referrer'),
        ),
        migrations.RemoveField(
            model_name='lab',
            name='test',
        ),
        migrations.AddField(
            model_name='lab',
            name='test',
            field=models.ForeignKey(help_text='Select a test for this patient', null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.Test', verbose_name='Select Test'),
        ),
        migrations.RemoveField(
            model_name='medication',
            name='drug',
        ),
        migrations.AddField(
            model_name='medication',
            name='drug',
            field=models.ForeignKey(help_text='Select a drug for this patient', null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.Drug', verbose_name='Select Drug'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='insurance',
        ),
        migrations.AddField(
            model_name='profile',
            name='insurance',
            field=models.ForeignKey(help_text='Select an insurance for this patient', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile_insurance', to='patients.Insurance', verbose_name='Select Insurance'),
        ),
        migrations.RemoveField(
            model_name='week',
            name='exercise',
        ),
        migrations.AddField(
            model_name='week',
            name='exercise',
            field=models.ForeignKey(help_text='Select exercise for this patient', null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.Exercise', verbose_name='Exercises for patient'),
        ),
    ]