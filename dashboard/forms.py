from django.forms import ModelForm
from .models import Project, ProjectApplication, ProjectAssignment
from user_profile.models import UserProfile


class EditProjectModelForm(ModelForm):
    class Meta:
        model = Project
        fields = ('__all__')
        exclude = ['user']


class ProjectApplicationModelForm(ModelForm):
    class Meta:
        model = ProjectApplication
        fields = ('__all__')
        exclude = ['user', 'project', 'date_applied']


class ProjectAssignmentModlForm(ModelForm):
    class Meta:
        model = ProjectAssignment
        fields = ('__all__')
        exclude = ['user', 'project']


class FreelanceAccountFormModel(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('__all__')
        exclude = ['user', 'profile_completed', 'account_type']


class ClientAccountFormModel(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('mobile', 'profile_image')
