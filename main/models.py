from django.db import models


class System(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    cost = models.DecimalField(decimal_places=2, max_digits=20, default=1000)

    system = models.ForeignKey(System, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OperatingMode(models.Model):
    value = models.FloatField()
    output = models.CharField(choices=[('Non-Regular', 'Non-Regular'), ('Regular', 'Regular')],
                              verbose_name='Operating Mode', max_length=30)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class DurationOfOperation(models.Model):
    value = models.FloatField()
    output = models.IntegerField()
    start_date = models.DateTimeField()

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class StructuralRisk(models.Model):
    value = models.FloatField()
    output = models.CharField(max_length=20)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class FunctionalRisk(models.Model):
    value = models.FloatField()
    output = models.CharField(max_length=20)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class FailureProbability(models.Model):
    value = models.FloatField()
    output = models.CharField(max_length=20)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class Damage(models.Model):
    value = models.FloatField()
    output = models.CharField(max_length=20)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class Rules(models.Model):
    operating_mode = models.FloatField(blank=True, null=True)
    duration_of_operation = models.FloatField(blank=True, null=True)
    structural_risk = models.FloatField(blank=True, null=True)
    functional_risk = models.FloatField(blank=True, null=True)
    failure_probability = models.FloatField(blank=True, null=True)
    damage = models.FloatField(blank=True, null=True)

    system_condition_assessment = models.FloatField()
    expert_assessment = models.FloatField()
    rule = models.CharField(max_length=200, default='')

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.rule

# class ExtraOption(models.Model):
#     operatingMode
#     duration of operation
#     cost
