$(document).ready(function(){
  <!--登録-->
  $('.regist').on('click', function(){
    var part = $('input[name="part"]').val();
    var name = $('input[name="name"]').val();
    var gender = $('select[name="gender"]').val();
    var contents = $('textarea[name="contents"]').val();
    var biko = $('textarea[name="biko"]').val();
    
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
    $('form').attr('action', url);
    $('form').submit();
    return false;
  });
});