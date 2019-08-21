from django.http.response import HttpResponse
from django.shortcuts import render
from django.db import transaction
from ..memoLogin import loginDb
from . import dbMainClass,const,constDef

class session():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__request = ""
    self.__valueList = {}
    self.__loginFlg = False

  # セッション登録処理
  def setSession(self):
    for col in self.__valueList:
      self.__request.session[col] = self.__valueList[col][1]

  # ログイン情報確認処理
  def loginCheckSession(self):
    if 'LOGINUSER' in self.__request.session and not self.__request.session['LOGINUSER'] == '' and self.__request.session['LOGINUSER'] is not None:
      self.__loginFlg = True
    elif 'LOGINPASSWORD' in self.__request.session and not self.__request.session['LOGINPASSWORD'] != '' and  self.__request.session['LOGINPASSWORD'] is not None:
      self.__loginFlg = True
   
  # ログアウト処理
  def logout(self):
    if 'LOGINUSER' in self.__request.session and not self.__request.session['LOGINUSER'] == '' and self.__request.session['LOGINUSER'] is not None:
      del self.__request.session['LOGINUSER']
    elif 'LOGINPASSWORD' in self.__request.session and not self.__request.session['LOGINPASSWORD'] != '' and  self.__request.session['LOGINPASSWORD'] is not None:
      del self.__request.session['LOGINPASSWORD']
    self.__request.session.clear()
    
  # リクエスト
  @property
  def request(self):
    return self.__request

  @request.setter
  def request(self,request):
    self.__request = request
    
  # 整形後配列
  @property
  def valueList(self):
    return self.__valueList

  @valueList.setter
  def valueList(self,valueList):
    self.__valueList = valueList

  # ログイン済みチェック
  @property
  def loginFlg(self):
    return self.__loginFlg

  @loginFlg.setter
  def loginFlg(self,loginFlg):
    self.__loginFlg = loginFlg