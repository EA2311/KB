from django.db import models


# Create your models here.
class System(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)


class Unit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    # ?
    #operating_mode = models.CharField(choices=[('Non-Regular', 'Non-Regular'), ('Regular', 'Regular')],
    #                                  verbose_name='Operating Mode')
    #duration_of_operation = models.IntegerField()
    #cost = models.DecimalField()

    system = models.ForeignKey(System, on_delete=models.CASCADE)


class StructuralRisk(models.Model):
    value = models.FloatField()
    output = models.CharField(max_length=20)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)


class FunctionalRisk(models.Model):
    value = models.FloatField()
    output = models.CharField(max_length=20)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)


class FailureProbability(models.Model):
    value = models.FloatField()
    output = models.CharField(max_length=20)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)


class Damage(models.Model):
    value = models.FloatField()
    output = models.CharField(max_length=20)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)


# class ExtraOption(models.Model):
#     operatingMode
#     duration of operation
#     cost
