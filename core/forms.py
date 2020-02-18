from allauth.account.forms import LoginForm


class LOGIN_FORM(LoginForm):
    def __init__(self, *args, **kwargs):
        self.fields['login'].widget = forms.TextInput(
            attrs={'type': 'email', 'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control'})
        return super(LOGIN_FORM, self).__init__(*args, **kwargs)
