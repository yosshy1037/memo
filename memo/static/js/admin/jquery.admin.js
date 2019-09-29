$(document).ready(function(){
  pager(1);
  
  <!--一覧表示の複数操作-->
  $('.relive').click(function() {
    var url = '/memo/memoAdList/';
    var listErea = '#resultErea';
    var atagErea = '#atag';
    var mesErea = '#mes';
    postData = {};
    postData['status'] = 'multiOpe';
    postData['pageNum'] = 1;
    postData['registStartDate'] = $('input[name="registStartDate"]').val();
    postData['registEndDate'] = $('input[name="registEndDate"]').val();
    postData['keyWord'] = $('input[name="keyWord"]').val();
    // チェックボックス状態取得
    var chList = [];
    $('#resultErea :checked').each(function() {
      chList.push($(this).val());
    });
    postData['list'] = chList;
    
    ajaxPost(url,postData,listErea,atagErea,mesErea);
    return false;
  });
  
  <!--メニュー画面 aタグ操作-->
  $('.linkClick').click(function() {
    var linkUrl = $(this).data('link');
    window.location.href=linkUrl;
    return false;
  });
});

<!--一覧の表示とAタグの制御-->
function pager(pageNum){
    var url = '/memo/memoAdList/';
    var listErea = '#resultErea';
    var atagErea = '#atag';
    var mesErea = '#mes';
    postData = {};
    postData['status'] = 'normal';
    postData['pageNum'] = pageNum;
    postData['registStartDate'] = $('input[name="registStartDate"]').val();
    postData['registEndDate'] = $('input[name="registEndDate"]').val();
    postData['keyWord'] = $('input[name="keyWord"]').val();
    
    // POST実行
    ajaxPost(url,postData,listErea,atagErea,mesErea);
    postData = {};
    return false;
}