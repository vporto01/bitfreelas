from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import *

# class ProjectForm(forms.ModelForm):
#     skills_required = forms.ModelMultipleChoiceField(
#         queryset=Skill.objects.all(),
#         widget=FilteredSelectMultiple("Skills", is_stacked=False)
#     )

#     class Meta:
#         model = Project
#         fields = '__all__'

# class ProjectAdmin(admin.ModelAdmin):
#     form = ProjectForm
#     list_display = ('title', 'skills_display')

#     def skills_display(self, obj):
#         return ", ".join([skill.name for skill in obj.skills_required.all()])

#     skills_display.short_description = 'Skills Required'

#     class Media:
#         js = ('projects/admin_scripts.js',)

# class FreelancerForm(forms.ModelForm):
#     skills = forms.ModelMultipleChoiceField(
#         queryset=Skill.objects.all(),
#         widget=FilteredSelectMultiple("Skills", is_stacked=False)
#     )

#     class Meta:
#         model = Freelancer
#         fields = '__all__'

# class FreelancerAdmin(admin.ModelAdmin):
#     form = FreelancerForm
#     list_display = ('user_name', 'skills_display')

#     def user_name(self, obj):
#         return obj.user.username

#     user_name.short_description = 'User Name'

#     def skills_display(self, obj):
#         return ", ".join([skill.name for skill in obj.skills.all()])

#     skills_display.short_description = 'Skills'

#     class Media:
#         js = ('projects/admin_scripts.js',)

# admin.site.register(Project, ProjectAdmin)
# admin.site.register(Client)
# admin.site.register(Freelancer, FreelancerAdmin)
# admin.site.register(Category)
# admin.site.register(Skill)
# admin.site.register(Currency)
admin.site.register(Projects)
