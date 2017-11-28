# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField


class MyForm(forms.Form):
    email = forms.EmailField(
        required=True,
        max_length=20,
        min_length=5,
        error_messages={
            'required': '邮箱名不能为空',
            'max_length': '邮箱名长度不得超过20个字符',
            'min_length': '邮箱名长度不得少于5个字符',
        }
    )

    captcha = CaptchaField(
        required=True,
        error_messages={
            'required': '验证码不能为空',
            'invalid': '验证码不正确'
        }
    )
