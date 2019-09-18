from django import forms

class registForm(forms.Form):
    registPart = forms.CharField(
      label='タイトル',
      max_length=15,
      widget=forms.TextInput(attrs={'class' : 'part'}),
      required=True,
    )
    registName = forms.CharField(
      label='名称（人名）',
      max_length=15,
      widget=forms.TextInput(attrs={'class' : 'name'}),
      required=True,
    )
    registContents = forms.CharField(
      label='内容',
      max_length=8000,
      widget=forms.Textarea(attrs={'rows': 10,'cols': 110,'class' : 'contents'}),
      required=True,
    )
    registBiko = forms.CharField(
      label='備考',
      max_length=8000,
      widget=forms.Textarea(attrs={'rows': 10,'cols': 110,'class' : 'contents'}),
      required=True,
    )