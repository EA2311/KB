from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from main.forms import RuleForm
from main.models import System, Unit, Rule


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

    def get_context_data(self, **kwargs):
        rules = Rule.objects.filter(unit=self.kwargs['id'])
        return set_context(super().get_context_data(**kwargs), rules=rules)


class AddRuleView(CreateView):
    model = Rule
    success_url = reverse_lazy('unit_list')
    form_class = RuleForm

    def form_valid(self, form):
        rule = form.save(commit=False)
        rule.unit = Unit.objects.get(id=self.kwargs['id'])
        rule.rule = f'If OM is {rule.operating_mode} and DoO is {rule.operating_mode} and SR is {rule.structural_risk} and FR is {rule.structural_risk} and D is {rule.damage} then Failure Probability is {rule.expert_assessment}'
        rule.save()
        return redirect('unit_list', pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        return set_context(super().get_context_data(**kwargs), pk=self.kwargs['pk'], unit=self.kwargs['id'])
