from django import forms
from .models import Project, Skill

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'skills_required': forms.CheckboxSelectMultiple(),
        }
