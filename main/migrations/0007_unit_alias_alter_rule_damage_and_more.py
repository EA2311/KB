# Generated by Django 4.2.7 on 2023-12-18 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_rule_damage_alter_rule_duration_of_operation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='alias',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='damage',
            field=models.CharField(blank=True, choices=[('Minimal', 'Minimal'), ('Low', 'Low'), ('Medium', 'Medium'), ('Critical', 'Critical')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='duration_of_operation',
            field=models.CharField(blank=True, choices=[('Minimal', 'Minimal'), ('Low', 'Low'), ('Medium', 'Medium'), ('Critical', 'Critical')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='expert_assessment',
            field=models.CharField(choices=[('Minimal', 'Minimal'), ('Low', 'Low'), ('Medium', 'Medium'), ('Critical', 'Critical')], max_length=20),
        ),
        migrations.AlterField(
            model_name='rule',
            name='failure_probability',
            field=models.CharField(blank=True, choices=[('Minimal', 'Minimal'), ('Low', 'Low'), ('Medium', 'Medium'), ('Critical', 'Critical')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='functional_risk',
            field=models.CharField(blank=True, choices=[('Minimal', 'Minimal'), ('Low', 'Low'), ('Medium', 'Medium'), ('Critical', 'Critical')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='operating_mode',
            field=models.CharField(blank=True, choices=[('Minimal', 'Minimal'), ('Low', 'Low'), ('Medium', 'Medium'), ('Critical', 'Critical')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='structural_risk',
            field=models.CharField(blank=True, choices=[('Minimal', 'Minimal'), ('Low', 'Low'), ('Medium', 'Medium'), ('Critical', 'Critical')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='system_condition_assessment',
            field=models.CharField(choices=[('Minimal', 'Minimal'), ('Low', 'Low'), ('Medium', 'Medium'), ('Critical', 'Critical')], max_length=20),
        ),
        migrations.AlterField(
            model_name='unit',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=1000, max_digits=20),
        ),
        migrations.AlterField(
            model_name='unit',
            name='damage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.damage'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='duration_of_operation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.durationofoperation'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='failure_probability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.failureprobability'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='functional_risk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.functionalrisk'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='operating_mode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.operatingmode'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='structural_risk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.structuralrisk'),
        ),
    ]