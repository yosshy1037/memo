from django import forms

class adminLoginForm(forms.Form):
    adLoginUser = forms.CharField(
      label='ユーザー名',
      max_length=8,
      widget=forms.TextInput(attrs={'class' : 'adLoginUser'}),
      required=True,
    )
    adLoginPassword = forms.CharField(
      label='パスワード',
      max_length=8,
      widget=forms.PasswordInput(attrs={'class' : 'adLoginPassword'}),
      required=True,
    )