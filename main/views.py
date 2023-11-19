from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from main.models import System, Unit


def set_context(context: dict, **kwargs) -> dict:
    if kwargs:
        for key, value in kwargs.items():
            context[key] = value

    return context


class AddSystemView(CreateView):
    model = System
    fields = '__all__'
    success_url = reverse_lazy('system_list')


class SystemListView(ListView):
    model = System


class UnitListView(ListView):
    template_name = 'unit_list.html'
    context_object_name = 'units'

    def get_queryset(self):
        return Unit.objects.filter(system__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        return set_context(super().get_context_data(**kwargs), pk=self.kwargs['pk'])


class UnitDetailView(DetailView):
    model = Unit

    def get_object(self, queryset=None):
        return Unit.objects.get(id=self.kwargs['id'])

