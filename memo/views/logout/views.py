from django.shortcuts import redirect
from django.views.generic import View
import traceback
from ...common import sessionClass,commonFuncClass,exceptionClass,logClass

## ログアウト
class logout(View):
  # POSTMethod
  def post(self, request, *args, **kwargs):
    self.__ses = sessionClass.session()
    self.__com = commonFuncClass.commonFunc()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    
    try:
      self.__ses.request = request
      # セッション情報削除
      self.__ses.logout()
      if str(request.GET.get('status')) == 'normal':
        return redirect("memo")
      else:
        return redirect("adLoginView")

    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")
    