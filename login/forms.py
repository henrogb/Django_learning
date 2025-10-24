from django import forms
from .models import RegistroUsuario
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="confirmar senha")
    
    
class Meta:
    model = RegistroUsuario
    fields = ['username']
    
    
def clean_password2(self):
    pw1 = self.cleaned_data.get('password1')
    pw2 = self.cleaned_data.get('password2')
    if pw1 != pw2:
        raise forms.ValidationError("As senhas não coincidem")
    return pw2


def save(self, commit=True):
    user = super().save(commit=False)
    user.senha = make_password(self.cleaned_data["password1"])
    if commit:
        user.save()
    return user
        