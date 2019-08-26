<!--一覧の表示とAタグの制御-->
function pager(pageNum){
    var part = $('input[name="part"]').val();
    var name = $('input[name="name"]').val();
    var registStartDate = $('input[name="registStartDate"]').val();
    var registEndDate = $('input[name="registEndDate"]').val();
    var gender = $('select[name="gender"]').val();
    var keyWord = $('input[name="keyWord"]').val();
    $.ajax({
      'url':'/memo/dataList/',
      'type':'POST',
      'data':{
        'pageNum':pageNum,
        'part':part,
        'name':name,
        'registStartDate':registStartDate,
        'registEndDate':registEndDate,
        'gender':gender,
        'keyWord':keyWord,
      },
      'dataType':'json',
      'success':function(response){
        $("#atag").html(response.atag);
        $("#resultErea").html(response.result);
      },
      'error':function(XMLHttpRequest, textStatus, errorThrown){
        alert("XMLHttpRequest : " + XMLHttpRequest.status + "/" + "errorThrown    : " + errorThrown.message );
      },
    });
    return false;
}
<!--詳細画面へ遷移-->
function detailSend(num){
  //document.memoForm.action = '/memo/memoDetail/?detailNum=' + num
  //$('form').attr('method', 'GET');
  //$('form').submit();
  window.open('/memo/memoDetail/?detailNum=' + num, '_blank');
  return false;
}