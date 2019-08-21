<!--一覧の表示とAタグの制御-->
function pager(pageNum,part,name){
    if(pageNum == 0){
      pageNum = 1;
    }
    $('input:hidden[name="pageNum"]').val(pageNum);
    $.ajax({
      'url':'/memo/dataList/',
      'type':'POST',
      'data':{
        'pageNum':pageNum,
        'partVal':part,
        'nameVal':name,
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