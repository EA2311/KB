from django.urls import path

from .views import AddSystemView, SystemListView, UnitListView, UnitDetailView, AddRuleView, UnitRulesListView, \
    RulesListView, UnitPredictionView

urlpatterns = [
    path("add_system/", AddSystemView.as_view(), name="add_system"),
    path("", SystemListView.as_view(), name="system_list"),
    path("<int:pk>/", UnitListView.as_view(), name="unit_list"),
    path("<int:pk>/<int:id>", UnitDetailView.as_view(), name="unit_detail"),

    path("<int:pk>/expert/<int:id>/add_rule", AddRuleView.as_view(), name="add_rule"),
    path("<int:pk>/expert", UnitRulesListView.as_view(), name="unit_rules_list"),
    path("<int:pk>/expert/<int:id>", RulesListView.as_view(), name="rules_list"),

    path("<int:pk>/prediction/<int:id>", UnitPredictionView.as_view(), name="unit_prediction"),

]
