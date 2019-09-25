from django import forms

class adminForm(forms.Form):
    registStartDate = forms.DateField(
      label='登録日',
      widget=forms.DateInput(attrs={'type':'date','class' : 'registStartDate'}),
      required=False,
    )
    registEndDate = forms.DateField(
      label='登録日',
      widget=forms.DateInput(attrs={'type':'date','class' : 'registEndDate'}),
      required=False,
    )
    keyWord = forms.CharField(
      label='キーワード',
      max_length=30,
      widget=forms.TextInput(attrs={'class' : 'keyWord'}),
      required=False,
    )