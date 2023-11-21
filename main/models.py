from django.db import models


class System(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class DurationOfOperation(models.Model):
    value = models.FloatField()
    output = models.IntegerField()
    start_date = models.DateTimeField()

    # unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class OperatingMode(models.Model):
    value = models.FloatField()
    output = models.CharField(choices=[('Non-Regular', 'Non-Regular'), ('Regular', 'Regular')],
                              verbose_name='Operating Mode', max_length=30)

    # unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class StructuralRisk(models.Model):
    value = models.FloatField()
    output = models.CharField(max_length=20)

    # unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class FunctionalRisk(models.Model):
    value = models.FloatField()
    output = models.CharField(max_length=20)

    # unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class FailureProbability(models.Model):
    value = models.FloatField()
    output = models.CharField(max_length=20)

    # unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class Damage(models.Model):
    value = models.FloatField()
    output = models.CharField(max_length=20)

    # unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class Unit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    system = models.ForeignKey(System, on_delete=models.CASCADE)

    cost = models.DecimalField(decimal_places=2, max_digits=20, default=1000)
    duration_of_operation = models.ForeignKey(DurationOfOperation, on_delete=models.CASCADE, null=True)
    operating_mode = models.ForeignKey(OperatingMode,  on_delete=models.CASCADE, null=True)
    structural_risk = models.ForeignKey(StructuralRisk, on_delete=models.CASCADE, null=True)
    functional_risk = models.ForeignKey(FunctionalRisk, on_delete=models.CASCADE, null=True)
    failure_probability = models.ForeignKey(FailureProbability, on_delete=models.CASCADE, null=True)
    damage = models.ForeignKey(Damage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


RULES_CHOICES = [('Minimal', 0), ('Low', 1), ('Medium', 2), ('Critical', 3)]


class Rule(models.Model):
    operating_mode = models.CharField(blank=True, null=True, choices=RULES_CHOICES, max_length=20)
    duration_of_operation = models.CharField(blank=True, null=True, choices=RULES_CHOICES, max_length=20)
    structural_risk = models.CharField(blank=True, null=True, choices=RULES_CHOICES, max_length=20)
    functional_risk = models.CharField(blank=True, null=True, choices=RULES_CHOICES, max_length=20)
    failure_probability = models.CharField(blank=True, null=True, choices=RULES_CHOICES, max_length=20)
    damage = models.CharField(blank=True, null=True, choices=RULES_CHOICES, max_length=20)

    system_condition_assessment = models.CharField(choices=RULES_CHOICES, max_length=20)
    expert_assessment = models.CharField(choices=RULES_CHOICES, max_length=20)
    rule = models.CharField(max_length=200, default='')

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.rule

# class ExtraOption(models.Model):
#     operatingMode
#     duration of operation
#     cost
