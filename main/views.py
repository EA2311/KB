from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.models import System


class AddSystemView(CreateView):
    model = System
    fields = '__all__'
    success_url = reverse_lazy('add_system')


