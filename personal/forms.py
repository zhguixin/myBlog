# -*- coding: UTF-8 -*-
'''
Created on 2018年1月11日

@author: zhguixin
'''
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
