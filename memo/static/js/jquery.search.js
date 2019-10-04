<!--一覧の表示とAタグの制御-->
function pager(pageNum,tempData){
    var url = '/memo/dataList/';
    var listErea = '#resultErea';
    var atagErea = '#atag';
    var mesErea = '#mes';
    postData = {};
    postData['status'] = 'normal';
    // Tempデータ(フォーム値履歴)使用
    if(tempData != "" & undefinedCheck(tempData) == false){
      tempData = String(tempData);
      tempData = tempData.split(',');
      postData['pageNum'] = tempData[5];
      postData['part'] = tempData[0];
      postData['name'] = tempData[1];
      postData['registStartDate'] = tempData[2];
      postData['registEndDate'] = tempData[3];
      postData['keyWord'] = tempData[4];
    }else{
      // 画面フォーム値使用
      postData['pageNum'] = pageNum;
      postData['part'] = $('input[name="part"]').val();
      postData['name'] = $('input[name="name"]').val();
      postData['registStartDate'] = $('input[name="registStartDate"]').val();
      postData['registEndDate'] = $('input[name="registEndDate"]').val();
      postData['keyWord'] = $('input[name="keyWord"]').val();
    }
    // POST実行
    ajaxPost(url,postData,listErea,atagErea,mesErea);
    return false;
}
<!--詳細画面へ遷移-->
function detailSend(num){
  // atagClicked番号取得
  var atagNum = $('.clicked').data('link');
  var url = '/memo/memoDetail/?detailNum=' + num + '&pageNum=' + atagNum;
  eurl = encodeURI(url);
  window.open(eurl, '_blank');
  return false;
}