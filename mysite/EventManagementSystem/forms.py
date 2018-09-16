from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from models import User, Slkf


class SlkfSignupForm(UserCreationForm):
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    position = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'firstName', 'lastName', 'position', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)

        user.position = self.cleaned_data['position']
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.USER_TYPE_CHOICES = 'SL'

        if commit:
            user.save()
            slkf = Slkf(user=user, memberName=user.first_name, position=user.position)
            slkf.save()
        return user

# class AssociationSignupForm(UserCreationForm)
