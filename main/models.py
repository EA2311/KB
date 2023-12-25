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
        return str(self.value)


class OperatingMode(models.Model):
    value = models.FloatField()
    output = models.CharField(choices=[('Non-Regular', 'Non-Regular'), ('Regular', 'Regular')],
                              verbose_name='Operating Mode', max_length=30)

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


class Unit(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=25, null=True)
    description = models.TextField(blank=True, null=True)
    system = models.ForeignKey(System, on_delete=models.CASCADE)

    cost = models.DecimalField(decimal_places=2, max_digits=20, default=1000, blank=True)
    duration_of_operation = models.ForeignKey(DurationOfOperation, on_delete=models.CASCADE, null=True, blank=True)
    operating_mode = models.ForeignKey(OperatingMode,  on_delete=models.CASCADE, null=True, blank=True)
    functional_risk = models.ForeignKey(FunctionalRisk, on_delete=models.CASCADE, null=True, blank=True)
    failure_probability = models.ForeignKey(FailureProbability, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


RULES_CHOICES = [('Minimal', 'Minimal'), ('Low', 'Low'), ('Medium', 'Medium'), ('Critical', 'Critical')]


class Rule(models.Model):
    operating_mode = models.CharField(blank=True, null=True, choices=RULES_CHOICES, max_length=20)
    duration_of_operation = models.CharField(blank=True, null=True, choices=RULES_CHOICES, max_length=20)
    functional_risk = models.CharField(blank=True, null=True, choices=RULES_CHOICES, max_length=20)
    failure_probability = models.CharField(blank=True, null=True, choices=RULES_CHOICES, max_length=20)

    system_condition_assessment = models.CharField(choices=RULES_CHOICES, max_length=20)
    expert_assessment = models.CharField(choices=RULES_CHOICES, max_length=20)
    rule = models.CharField(max_length=200, default='')

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.rule

