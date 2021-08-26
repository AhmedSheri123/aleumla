from django import forms
from django.forms import widgets


class signup_form(forms.Form):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'data-layer':"262bbc36-d8d7-4e16-b709-0ab2414173b6", 'class':"rectangle4", 'style':"padding-left:50px; color:#855B58;", 'placeholder':"اسم المستخدم"}))
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(attrs={'data-layer':"c9c14c65-e5a7-4c0f-80a8-c3c25a31637b", 'class':"rectangle5", 'style':"padding-left:50px; color:#855B58;", 'placeholder':"بريد الالكتروني"}))
    password1 = forms.CharField(label="", min_length=5, widget=forms.PasswordInput(attrs={'data-layer':"35cebe30-93e9-45e5-812a-358db706c43b", 'class':"rectangle6", 'style':"padding-left:50px; color:#855B58;", 'placeholder':"كلمة المرور"}))
    password2 = forms.CharField(label="", min_length=5, widget=forms.PasswordInput(attrs={'data-layer':"ea695c8a-df75-4e07-bc6f-68b719ab655a", 'class':"rectangle8", 'style':"padding-left:50px; color:#855B58; ", 'placeholder':"تاكيد كلمة المرور"}))


class signin_form(forms.Form):
    username_or_email = forms.CharField(label="", widget=forms.TextInput(attrs={'data-layer':"fc4b965b-94e6-4fc7-9f95-e52a9b20642b", 'class':"rectangle5", 'style':"padding-left:50px; color:#855B58;", 'placeholder':"اسم المستخدم او بريد الالكتروني"}))
    password = forms.CharField(label="", min_length=4, widget=forms.PasswordInput(attrs={'data-layer':"57983465-d2bd-4864-b6cb-0fb2a8e86a60", 'class':"rectangle6", 'style':"padding-left:50px; color:#855B58;", 'placeholder':"كلمة المرور"}))



class profile_form(forms.Form):
    first_name = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'style':"padding-left:50px; color: #855B58;", 'data-layer':"421d49a6-eb13-4c6a-9525-185f23df4541", 'class':"rectangle10", 'value':"", 'placeholder':"اسم الاول"}))
    last_name = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'style':"padding-left:50px; color: #855B58;", 'data-layer':"24693882-5ca7-4caa-8aba-febe4b59040a", 'class':"rectangle11", 'value':"", 'placeholder':"اسم النسبة"}))
    phone = forms.CharField(label='', max_length=15, widget=forms.NumberInput(attrs={'style':"padding-left:50px; color: #855B58;", 'data-layer':"75230d8d-c2a7-4f6c-9270-871314c1f27e", 'class':"rectangle13", 'value':"", 'placeholder':"رقم الهاتف"}))
    city = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'style':"padding-left:50px; color: #855B58;", 'data-layer':"a4e703ad-552c-4baf-9ecc-f6d7101586ed", 'class':"rectangle12", 'value':"", 'placeholder':"المدينة"}))
    img = forms.ImageField(label="", required=False, widget=forms.FileInput(attrs={"style":"display:none;", 'class':"img_field"}))


class resetpassword(forms.Form):
    password1 = forms.CharField(label="", min_length=5, widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"كلمة المرور"}))
    password2 = forms.CharField(label="", min_length=5, widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"تاكيد"}))