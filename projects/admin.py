from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import *

class ProjectForm(forms.ModelForm):
    skills_required = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=FilteredSelectMultiple("Skills", is_stacked=False)
    )

    class Meta:
        model = Project
        fields = '__all__'

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('title', 'skills_display')

    def skills_display(self, obj):
        return ", ".join([skill.name for skill in obj.skills_required.all()])

    skills_display.short_description = 'Skills Required'

    class Media:
        js = ('projects/admin_scripts.js',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Client)
admin.site.register(Freelancer)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Currency)
