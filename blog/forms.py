# -*- coding: UTF-8 -*-
'''
Created on 2018年1月6日

@author: zhguixin
'''
from django import forms
from .models import Comment

'''
实现评论功能
'''
'''
class CommentForm(forms.ModelForm):
    # 继承ModelForm,在表单的内部类 Meta 里指定一些和表单相关的东西
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
'''

class CommentForm(forms.Form):
    # 继承Form
    name = forms.CharField(label='昵称', max_length=16, error_messages={
        'required':'请填写您的昵称',
        'max_length':'昵称呼太长咯'
    })

    email = forms.EmailField(label='邮箱', error_messages={
        'required':'请填写您的邮箱',
        'invalid':'邮箱格式不正确'
    })

    content = forms.CharField(label='评论', error_messages={
        'required':'请填写您的评论内容！',
        'max_length':'评论内容太长咯'
    }, widget=forms.Textarea)

if __name__ == '__main__':
    pass