from django import forms

class searchForm(forms.Form):
    part = forms.CharField(
      label='タイトル',
      max_length=15,
      widget=forms.TextInput(attrs={'class' : 'part'}),
      required=False,
    )
    name = forms.CharField(
      label='名称（人名）',
      max_length=15,
      widget=forms.TextInput(attrs={'class' : 'name'}),
      required=False,
    )
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