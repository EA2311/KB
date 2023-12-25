from django import forms

from main.models import Rule


class RuleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RuleForm, self).__init__(*args, **kwargs)
        self.fields['operating_mode'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['duration_of_operation'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['functional_risk'].widget.attrs = {
            'class': 'form-control'
        }

        self.fields['system_condition_assessment'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['expert_assessment'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Rule
        exclude = ['unit', 'failure_probability', 'rule']
