from django.shortcuts import redirect
from django.views.generic import View
from ...common import sessionClass

## ログアウト
class logout(View):
  # POSTMethod
  def post(self, request, *args, **kwargs):
    self.__ses = sessionClass.session()
    self.__ses.request = request
    # セッション情報削除
    self.__ses.logout()
    return redirect("memo")