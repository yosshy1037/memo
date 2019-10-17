$(document).ready(function(){
  <!--メニュー画面 aタグ操作-->
  $('.linkClick').click(function() {
    var linkUrl = $(this).data('link');
    window.location.href=linkUrl;
    return false;
  });
});