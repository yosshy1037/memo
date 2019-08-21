$(document).ready( function(){
  if(pageNumber == ""){
      pageNumber = 0;
  }
  // ページャ制御
  pager(pageNumber,part,name);
  
  // 新規登録画面へ遷移
  $('.registPage').on('click', function(){
    $('form').attr('action', '/memo/memoRegist/');
    $('form').submit();
  });
});