from django.urls import path

from . import views
from .views import AddSystemView, SystemListView, UnitListView, UnitDetailView

#app_name = "main"

urlpatterns = [
    path("add_system/", AddSystemView.as_view(), name="add_system"),
    path("", SystemListView.as_view(), name="system_list"),
    path("<int:pk>/", UnitListView.as_view(), name="unit_list"),
    path("<int:pk>/<int:id>", UnitDetailView.as_view(), name="unit_detail"),

]
