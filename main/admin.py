from django.contrib import admin

from main.models import System, Unit, FunctionalRisk, FailureProbability, OperatingMode, \
    DurationOfOperation, Rule

admin.site.register(System)
admin.site.register(Unit)
admin.site.register(OperatingMode)
admin.site.register(DurationOfOperation)
admin.site.register(FunctionalRisk)
admin.site.register(FailureProbability)
admin.site.register(Rule)

