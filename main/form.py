from django import forms
from .models import Group, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateGroup(forms.ModelForm):
	group_name = forms.CharField(max_length=30)

	class Meta:
		model = Group 
		fields = '__all__'

class SendMessage(forms.ModelForm):
	class Meta:
		model = Message
		fields = ('group_belong', 'content', 'sender',)


class RegisterUser(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2',)