# Generated by Django 4.2.7 on 2023-11-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_damage_unit_remove_durationofoperation_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='damage',
            field=models.CharField(blank=True, choices=[('Minimal', 0), ('Low', 1), ('Medium', 2), ('Critical', 3)], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='duration_of_operation',
            field=models.CharField(blank=True, choices=[('Minimal', 0), ('Low', 1), ('Medium', 2), ('Critical', 3)], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='expert_assessment',
            field=models.CharField(choices=[('Minimal', 0), ('Low', 1), ('Medium', 2), ('Critical', 3)], max_length=20),
        ),
        migrations.AlterField(
            model_name='rule',
            name='failure_probability',
            field=models.CharField(blank=True, choices=[('Minimal', 0), ('Low', 1), ('Medium', 2), ('Critical', 3)], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='functional_risk',
            field=models.CharField(blank=True, choices=[('Minimal', 0), ('Low', 1), ('Medium', 2), ('Critical', 3)], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='operating_mode',
            field=models.CharField(blank=True, choices=[('Minimal', 0), ('Low', 1), ('Medium', 2), ('Critical', 3)], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='structural_risk',
            field=models.CharField(blank=True, choices=[('Minimal', 0), ('Low', 1), ('Medium', 2), ('Critical', 3)], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='system_condition_assessment',
            field=models.CharField(choices=[('Minimal', 0), ('Low', 1), ('Medium', 2), ('Critical', 3)], max_length=20),
        ),
    ]