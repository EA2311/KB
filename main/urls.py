from django.urls import path

from . import views
from .views import AddSystemView, SystemListView, UnitListView, UnitDetailView, AddRuleView

#app_name = "main"

urlpatterns = [
    path("add_system/", AddSystemView.as_view(), name="add_system"),
    path("", SystemListView.as_view(), name="system_list"),
    path("<int:pk>/", UnitListView.as_view(), name="unit_list"),
    path("<int:pk>/<int:id>", UnitDetailView.as_view(), name="unit_detail"),
    path("<int:pk>/<int:id>/add_rule", AddRuleView.as_view(), name="add_rule"),

]
