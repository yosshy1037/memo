from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from . import forms

def memo(request):
  part = request.POST.get('part');
  name = request.POST.get('name');
  
  if request.POST.get('pageNum') == None:
    part = "";
  else:
    part = request.POST.get('part');
    
  if request.POST.get('name') == None:
    name = "";
  else:
    name = request.POST.get('name');
  
  if request.POST.get('pageNum') == None:
    pageNum = 1;
  else:
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