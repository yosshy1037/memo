$(document).ready( function(){
  // ページャ制御
  pager(1);
  
  // 新規登録画面へ遷移
  $('.registPage').on('click', function(){
    $('form').attr('action', '/memo/memoRegist/');
    $('form').submit();
  });
});