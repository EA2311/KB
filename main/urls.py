from django.urls import path

from . import views
from .views import AddSystemView

#app_name = "main"

urlpatterns = [
    path("add_system/", AddSystemView.as_view(), name="add_system"),
]
