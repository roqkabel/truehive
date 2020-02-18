from django.forms import ModelForm, CharField
from .models import UserProfile


class FreelancerForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('__all__')
        exclude = ['user',
                   'profile_completed',
                   'account_type']


class ClientForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('mobile', 'profile_image')
