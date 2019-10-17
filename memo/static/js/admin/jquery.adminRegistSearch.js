$(document).ready(function(){
  resultForm();
});

<!--登録処理-->
function registIdRegist(){
    var url = '/memo/memoAdRegistSearchList/';
    var listErea = '#resultErea';
    var atagErea = '';
    var mesErea = '#mes';
    postData = {};
    postData['status'] = 'regist';
    postData['loginUserId'] = $('input[name="loginUserId"]').val();
    postData['registId'] = $('input[name="registId"]').val();
    postData['resultLoginUserId'] = $('input[name="resultLoginUserId"]').val();
    postData['resultRegistId'] = $('input[name="resultRegistId"]').val();
    
    ajaxPost(url,postData,listErea,atagErea,mesErea);
    return false;
}

<!--更新処理-->
function registIdUpdate(id){
    var url = '/memo/memoAdRegistSearchList/';
    var listErea = '#resultErea';
    var atagErea = '';
    var mesErea = '#mes';
    postData = {};
    postData['status'] = 'update';
    postData['id'] = id
    postData['loginUserId'] = $('input[name="loginUserId"]').val();
    postData['registId'] = $('input[name="registId"]').val();
    var col = "resultLoginUserIdSelect_" + id
    postData[col] = $('[name="' + col + '"] option:selected').text();
    
    ajaxPost(url,postData,listErea,atagErea,mesErea);
    return false;
}
<!--削除処理-->
function registIdDelete(id){
    var url = '/memo/memoAdRegistSearchList/';
    var listErea = '#resultErea';
    var atagErea = '';
    var mesErea = '#mes';
    postData = {};
    postData['status'] = 'delete';
    postData['id'] = id
    postData['loginUserId'] = $('input[name="loginUserId"]').val();
    postData['registId'] = $('input[name="registId"]').val();
    
    ajaxPost(url,postData,listErea,atagErea,mesErea);
    return false;
}

<!--一覧の表示の制御-->
function resultForm(){
    var url = '/memo/memoAdRegistSearchList/';
    var listErea = '#resultErea';
    var atagErea = '#atag';
    var mesErea = '#mes';
    postData = {};
    postData['status'] = 'normal';
    postData['loginUserId'] = $('input[name="loginUserId"]').val();
    postData['registId'] = $('input[name="registId"]').val();
    
    // POST実行
    ajaxPost(url,postData,listErea,atagErea,mesErea);
    return false;
}