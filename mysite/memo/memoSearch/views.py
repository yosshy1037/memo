from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from . import models
from . import forms

def memo(request):
  part = request.POST.get('part');
  name = request.POST.get('name');
  pageNum = request.POST.get('pageNum');
  if part=="":
    message = '入力してください'
  else:
    message = ''
  
  form = forms.MemoSearchForm(request.POST or None);
  d = {
    'form': form,
    'partErr' : message,
    'pageNum' : pageNum,
    'part' : part,
    'name' : name,
  }
  return render(request, 'memoSearch/memoSearchView.html', d )