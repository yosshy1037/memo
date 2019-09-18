$(document).ready(function(){
  <!--テスト再度実行する-->
  $('.returnTest').on('click', function(){
    var url = "/memo/memoTest/";
    window.location.href=url;
    return false;
  });
});