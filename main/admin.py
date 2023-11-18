from django.contrib import admin

from main.models import System, Unit, StructuralRisk, FunctionalRisk, FailureProbability, Damage, OperatingMode, \
    DurationOfOperation, Rules

admin.site.register(System)
admin.site.register(Unit)
admin.site.register(OperatingMode)
admin.site.register(DurationOfOperation)
admin.site.register(StructuralRisk)
admin.site.register(FunctionalRisk)
admin.site.register(FailureProbability)
admin.site.register(Damage)
admin.site.register(Rules)

