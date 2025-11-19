from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30, min_length=3)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password') 
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Password do not match')
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30, min_length=3)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)