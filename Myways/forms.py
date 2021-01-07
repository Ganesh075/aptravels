from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Myways.models import Exfd,Data

class Usregis(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["first_name","last_name","email","username"]
		widgets = {
		"first_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your First Name",
			"required":True,
			}),
		"last_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Last Name",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Emailid",
			"required":True,
			}),
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your UserName",
			"required":True,
			}),
		}

class Upd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			}),
		}

class Pad(forms.ModelForm):
	class Meta:
		model = Exfd
		fields = ["rollno","collegename","age","gender","impf"]
		widgets = {
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Update your age",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			"title":"gender",
			}),
		"rollno":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update your Roll Number",
			}),
		"collegename":forms.Select(attrs={
			"class":"form-control",
			"title":"select collegename",
			}),
		}


class Busdata(forms.ModelForm):
	class Meta:
		model = Data
		fields = ["source","destination","busid","busclass","timmings","distance","cost","busim"]
		widgets = {
		"source":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Source location",
			"required":True,
			}),
		"destination":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Destination location",
			"required":True,
			}),
		"busid":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Bus number",
			"required":True,
			}),
		"busclass":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Select class",
			"required":True,
			}),
		"timmings":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Bus Timmings",
			"required":True,
			}),
		"distance":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter the distance",
			}),
		"cost":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter cost",
			}),
		}

class usdate(forms.ModelForm):
	class Meta:
		model = Data
		fields = ["da"]
