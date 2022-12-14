from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Inform a valid email address.',
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2', )


class ResetPassword(PasswordResetForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('email')


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('email',)
