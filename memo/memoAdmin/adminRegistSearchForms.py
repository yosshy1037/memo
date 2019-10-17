from django import forms

class adminRegistSearchForm(forms.Form):
    loginUserId = forms.CharField(
      label='ユーザーID',
      max_length=8,
      widget=forms.TextInput(attrs={'class' : 'loginUserId'}),
      required=False,
    )
    registId = forms.CharField(
      label='作成者ID',
      max_length=25,
      widget=forms.TextInput(attrs={'class' : 'registId'}),
      required=False,
    )