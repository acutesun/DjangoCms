from django import forms


class LoginForm(forms.Form):
    uid = forms.CharField(required=True)   # 这里的字段username要和前端的key相同
    pwd = forms.CharField(required=True, min_length=3)  # 不能为空并且长度不能小于3