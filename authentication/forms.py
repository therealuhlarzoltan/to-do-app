from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)


    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user


class UserUpdateForm(UserChangeForm):
    
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')