# Generated by Django 4.2.7 on 2023-11-19 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_rules_rule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='damage',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='durationofoperation',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='failureprobability',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='functionalrisk',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='operatingmode',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='structuralrisk',
            name='unit',
        ),
        migrations.AddField(
            model_name='unit',
            name='damage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.damage'),
        ),
        migrations.AddField(
            model_name='unit',
            name='duration_of_operation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.durationofoperation'),
        ),
        migrations.AddField(
            model_name='unit',
            name='failure_probability',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.failureprobability'),
        ),
        migrations.AddField(
            model_name='unit',
            name='functional_risk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.functionalrisk'),
        ),
        migrations.AddField(
            model_name='unit',
            name='operating_mode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.operatingmode'),
        ),
        migrations.AddField(
            model_name='unit',
            name='structural_risk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.structuralrisk'),
        ),
    ]