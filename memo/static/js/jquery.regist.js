$(document).ready(function(){
  <!--登録-->
  $('.regist').on('click', function(){
    var part = $('input[name="registPart"]').val();
    var name = $('input[name="registName"]').val();
    var gender = $('select[name="registGender"]').val();
    var contents = $('textarea[name="registContents"]').val();
    var biko = $('textarea[name="registBiko"]').val();
    
    $.ajax({
      'url':'/memo/regist/',
      'type':'POST',
      'data':{
        'part': part,
        'name': name,
        'gender': gender,
        'contents': contents,
        'biko': biko,
      },
      'dataType':'json',
      'success':function(response){
        $(".registMessage").html("<p class='mes'>" + response.result + "</p>");
      },
      'error':function(XMLHttpRequest, textStatus, errorThrown){
        alert("XMLHttpRequest : " + XMLHttpRequest.status + "/" + "errorThrown    : " + errorThrown.message );
      },
    });
    return false;
  });
  
  <!--検索画面へ戻る-->
  $('.searchReturn').on('click', function(){
    var url = "/memo/memoSearch/";
    window.location.href=url;
    return false;
  });
});