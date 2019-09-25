<!--一覧の表示とAタグの制御-->
function pager(pageNum){
    var url = '/memo/dataList/';
    var listErea = '#resultErea';
    var atagErea = '#atag';
    var mesErea = '#mes';
    postData = {};
    postData['status'] = 'normal';
    postData['pageNum'] = pageNum;
    postData['part'] = $('input[name="part"]').val();
    postData['name'] = $('input[name="name"]').val();
    postData['registStartDate'] = $('input[name="registStartDate"]').val();
    postData['registEndDate'] = $('input[name="registEndDate"]').val();
    postData['keyWord'] = $('input[name="keyWord"]').val();
    
    // POST実行
    ajaxPost(url,postData,listErea,atagErea,mesErea);
    return false;
}
<!--詳細画面へ遷移-->
function detailSend(num){
  //$('form').attr('action', '/memo/memoDetail/?detailNum=' + num);
  //$('form').attr('method', 'GET');
  //$('form').submit();
  window.open('/memo/memoDetail/?detailNum=' + num, '_blank');
  return false;
}