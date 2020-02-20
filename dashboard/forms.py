from django.forms import ModelForm
from .models import Project


class EditProjectModelForm(ModelForm):
    class Meta:
        model = Project
        fields = ('__all__')
        exclude = ['user']
