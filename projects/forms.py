from django import forms
from .models import *
from django.contrib.admin.widgets import FilteredSelectMultiple

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'skills_required': forms.CheckboxSelectMultiple(),
        }

class FreelancerForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=FilteredSelectMultiple("Skills", is_stacked=False)
    )

    class Meta:
        model = Freelancer
        fields = '__all__'