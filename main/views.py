from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
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
    # template_name = 'main/prediction.html'
    context_object_name = 'units'

    def get_queryset(self):
        return Unit.objects.filter(system__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        return set_context(super().get_context_data(**kwargs), pk=self.kwargs['pk'], data_points=[
            {"label": "TPMEP", "y": 2},
            {"label": "BP", "y": 3},
            {"label": "CS PSC", "y": 1},
            {"label": "ED PSC", "y": 1},
            {"label": "BDS", "y": 1},
            {"label": "ME", "y": 1},
            {"label": "SPP", "y": 1},
            {"label": "RACSME", "y": 1},
            {"label": "MCME", "y": 1},
            {"label": "CS", "y": 2},
            {"label": "FFS", "y": 4},
        ])


class UnitDetailView(DetailView):
    model = Unit

    def get_object(self, queryset=None):
        return Unit.objects.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        rules = Rule.objects.filter(unit=self.kwargs['id'])
        return set_context(super().get_context_data(**kwargs), rules=rules, pk=self.kwargs['pk'], id=self.kwargs['id'],
                           data_points_apr=[
                               {"label": "1000", "y": 0.169021143},
                               {"label": "5000", "y": 0.205413252},
                               {"label": "10000", "y": 0.263755837},
                               {"label": "15000", "y": 0.338669198},
                               {"label": "20000", "y": 0.434859859},
                           ], data_points_apos=[
                {"label": "1000", "y": 0.165171911},
                {"label": "5000", "y": 0.18495024},
                {"label": "10000", "y": 0.213809796},
                {"label": "15000", "y": 0.247172584},
                {"label": "20000", "y": 0.285741288},

            ])


class AddRuleView(CreateView):
    model = Rule
    success_url = reverse_lazy('unit_list')
    form_class = RuleForm

    def form_valid(self, form):
        rule = form.save(commit=False)
        rule.unit = Unit.objects.get(id=self.kwargs['id'])
        rule.rule = f'If OM is {rule.operating_mode} and DoO is {rule.operating_mode} and FR is {rule.functional_risk} and FP is {rule.failure_probability} then Failure Probability is {rule.expert_assessment}'
        rule.save()
        return redirect('rules_list', pk=self.kwargs['pk'], id=rule.unit.id)

    def get_context_data(self, **kwargs):
        return set_context(super().get_context_data(**kwargs), pk=self.kwargs['pk'], unit=self.kwargs['id'])


class UnitRulesListView(ListView):
    template_name = 'main/unit_rules_list.html'
    context_object_name = 'units'

    def get_queryset(self):
        return Unit.objects.filter(system__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        return set_context(super().get_context_data(**kwargs), pk=self.kwargs['pk'])


class RulesListView(ListView):
    template_name = 'main/rules_list.html'
    context_object_name = 'rules'

    def get_queryset(self):
        return Rule.objects.filter(unit=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        return set_context(super().get_context_data(**kwargs), pk=self.kwargs['pk'], id=self.kwargs['id'])


class UnitPredictionView(View):

    def get(self, request, pk, id):
        unit = Unit.objects.get(system__id=pk, id=id)
        context = {"unit": unit,  'data_points_apr':[
            {"label": "1000", "y": 0.169021143},
            {"label": "5000", "y": 0.205413252},
            {"label": "10000", "y": 0.263755837},
            {"label": "15000", "y": 0.338669198},
            {"label": "20000", "y": 0.434859859},
        ], 'data_points_apos':[
            {"label": "1000", "y": 0.165171911},
            {"label": "5000", "y": 0.18495024},
            {"label": "10000", "y": 0.213809796},
            {"label": "15000", "y": 0.247172584},
            {"label": "20000", "y": 0.285741288},

        ]}
        return render(request, "main/prediction.html", context)
