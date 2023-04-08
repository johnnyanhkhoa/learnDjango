from django import forms
from module_1.models import *


class FormCreateRifle(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Name: ', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Input name",
    }))
    place_of_origin = forms.CharField(max_length=264, label='Place of origin: ', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Input place of origin",
    }))

    class Meta:
        model = Rifle
        fields = ['name', 'place_of_origin']


class FormSignup(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Email",
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Mật khẩu",
    }))
    password_confirm = forms.CharField(label='Password confirm', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Xác nhận Mật khẩu",
    }))

    class Meta:
        model = User
        fields = ['email', 'password']


class FormAuthor(forms.ModelForm):
    name = forms.CharField(max_length=150, label='Name: ', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Input author name",
    }))

    class Meta:
        model = Author
        fields = ['name']



# Get queryset
author_list = Author.objects.only('id')
class FormBook(forms.ModelForm):
    name = forms.CharField(max_length=150, label='Book name: ', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Input book name",
    }))
    author = forms.ModelChoiceField(required=False, queryset=author_list ,widget=forms.Select(attrs={
        "class": "form-control", "placeholder": "Author name",
    }))

    class Meta:
        model = Book
        fields = ['name','author']