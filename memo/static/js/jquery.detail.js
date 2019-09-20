$(document).ready(function(){
  <!--更新-->
  $('.update').on('click', function(){
    var url = '/memo/update/'
    var mesErea = '.detailMessage'
    postData = {}
    postData['part'] = $('input[name="detailPart"]').val();
    postData['name'] = $('input[name="detailName"]').val();
    postData['contents'] = $('textarea[name="detailContents"]').val();
    postData['biko'] = $('textarea[name="detailBiko"]').val();
    postData['detailQuery'] = $(location).attr('search');
    postData['status'] = 'update'
    ajaxPost(url,postData,mesErea);
    return false;
  });
  
  <!--削除-->
  $('.delete').on('click', function(){
    var url = '/memo/update/'
    var mesErea = '.detailMessage'
    postData = {}
    postData['detailQuery'] = $(location).attr('search');
    postData['status'] = 'delete'
    ajaxPost(url,postData,mesErea);
    return false;
  });
  
  <!--検索画面へ戻る-->
  $('.detailClose').on('click', function(){
    window.open('about:blank','_self').close();
    return false;
  });
});