$(document).ready( function(){
  // ページャ制御
  pager(1);
  
  // 新規登録画面へ遷移
  $('.registPage').on('click', function(){
    // atagClicked番号取得
    var atagNum = $('.clicked').data('link');
    var url = '/memo/memoRegist/?pageNum=' + atagNum;
    eurl = encodeURI(url);
    $('form').attr('action', eurl);
    $('form').submit();
  });
});