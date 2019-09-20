$(document).ready(function(){
  <!--登録-->
  $('.regist').on('click', function(){
    var url = '/memo/regist/'
    var mesErea = '.registMessage'
    postData = {}
    postData['part'] = $('input[name="registPart"]').val();
    postData['name'] = $('input[name="registName"]').val();
    postData['contents'] = $('textarea[name="registContents"]').val();
    postData['biko'] = $('textarea[name="registBiko"]').val();
    ajaxPost(url,postData,mesErea);
    return false;
  });
  
  <!--検索画面へ戻る-->
  $('.searchReturn').on('click', function(){
    var url = "/memo/memoSearch/";
    window.location.href=url;
    return false;
  });
});