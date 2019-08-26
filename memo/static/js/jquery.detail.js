$(document).ready(function(){
  <!--更新-->
  $('.update').on('click', function(){
    var part = $('input[name="detailPart"]').val();
    var name = $('input[name="detailName"]').val();
    var gender = $('select[name="detailGender"]').val();
    var contents = $('textarea[name="detailContents"]').val();
    var biko = $('textarea[name="detailBiko"]').val();
    var detailQuery = $(location).attr('search');
    $.ajax({
      'url':'/memo/update/',
      'type':'POST',
      'data':{
        'part': part,
        'name': name,
        'gender': gender,
        'contents': contents,
        'biko': biko,
        'detailQuery': detailQuery,
      },
      'dataType':'json',
      'success':function(response){
        $(".detailMessage").html("<p class='mes'>" + response.result + "</p>");
      },
      'error':function(XMLHttpRequest, textStatus, errorThrown){
        alert("XMLHttpRequest : " + XMLHttpRequest.status + "/" + "errorThrown    : " + errorThrown.message );
      },
    });
    return false;
  });
  
  <!--検索画面へ戻る-->
  $('.detailClose').on('click', function(){
    window.open('about:blank','_self').close();
    return false;
  });
});