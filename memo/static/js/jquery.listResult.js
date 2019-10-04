$(document).ready( function(){
  // ページャ制御
  pager(1,tempData);

  // 検索処理
  $('.search').on('click', function(){
    var atagNum = $('.clicked').data('link');
    pager(atagNum,'');
    return false;
  });
  
  // クリア処理
  $('.clear').on('click', function(){
    document.getElementsByName("part")[0].value = "";
    document.getElementsByName("name")[0].value = "";
    document.getElementsByName("registStartDate")[0].value = getDate(2);
    document.getElementsByName("registEndDate")[0].value = getDate(0);
    document.getElementsByName("keyWord")[0].value = "";
    pager(1,'');
    return false;
  });
  
  // 新規登録画面へ遷移
  $('.registPage').on('click', function(){
    // atagClicked番号取得
    var atagNum = $('.clicked').data('link');
    var url = '/memo/memoRegist/?pageNum=' + atagNum;
    eurl = encodeURI(url);
    $('form').attr('action', eurl);
    $('form').submit();
    return false;
  });
});