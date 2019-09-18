from django import forms

class loginForm(forms.Form):
    loginUser = forms.CharField(
      label='ユーザー名',
      max_length=8,
      widget=forms.TextInput(attrs={'class' : 'loginUser'}),
      required=True,
    )
    loginPassword = forms.CharField(
      label='パスワード',
      max_length=8,
      widget=forms.PasswordInput(attrs={'class' : 'loginPassword'}),
      required=True,
    )