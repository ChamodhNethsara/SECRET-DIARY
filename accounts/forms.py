from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        label='Username',
        help_text='Enter Your Username Here')

    password = forms.PasswordInput()

    

    