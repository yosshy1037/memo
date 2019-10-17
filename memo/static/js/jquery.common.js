// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function(){
  <!--メニュータグ操作-->
  $('#menu').click(function() {
    var linkUrl = '/memo/memoAdMenu/';
    window.location.href=linkUrl;
    return false;
  });
  <!--ログアウト管理画面-->
  $('#logoutAdmin').on('click', function(){
    var url = "/memo/logout/";
    url = url + "?status=" + 'admin';
    $('form').attr('action', url);
    $('form').submit();
    return false;
  });
  <!--ログアウト-->
  $('#logoutNormal').on('click', function(){
    var url = "/memo/logout/";
    url = url + "?status=" + 'normal';
    $('form').attr('action', url);
    $('form').submit();
    return false;
  });
  <!--ログイン画面へ戻る-->
  $('.loginReturn').on('click', function(){
    var url = "/memo/logout/";
    var status = $('input[name="dispStatus"]').val();
    url = url + "?status=" + status;
    $('form').attr('action', url);
    $('form').submit();
    return false;
  });
});

// AjaxPost用関数
function ajaxPost(url,postData,mesErea){
    $.ajax({
      'url':url,
      'type':'POST',
      'data':{
        'postData': JSON.stringify(postData),
      },
      'dataType':'json',
      'success':function(response){
        $(mesErea).html("<p class='mes'>" + response.result + "</p>");
      },
      'error':function(XMLHttpRequest, textStatus, errorThrown){
        alert("XMLHttpRequest : " + XMLHttpRequest.status + "/" + "errorThrown    : " + errorThrown.message );
      },
    });
}

// AjaxPost用関数
function ajaxPost(url,postData,listErea,atagErea,mesErea){
    $.ajax({
      'url':url,
      'type':'POST',
      'data':{
        'postData': JSON.stringify(postData),
      },
      'dataType':'json',
      'success':function(response){
        $(atagErea).html(response.atag);
        $(listErea).html(response.result);
        $(mesErea).html(response.status);
      },
      'error':function(XMLHttpRequest, textStatus, errorThrown){
        alert("XMLHttpRequest : " + XMLHttpRequest.status + "/" + "errorThrown    : " + errorThrown.message );
      },
    });
}

// undefinedCheck用関数
function undefinedCheck(value){
  var flg = false;
  if(typeof value === "undefined"){
    flg = true;
  }
  return flg;
}

// 現在日時取得関数
function getDate(interval){
  // 日付取得
  var today = new Date();
  var year = today.getFullYear() - interval;
  var month = today.getMonth() + 1;
  var day = today.getDate();
  var hour = today.getHours();
  var sec = today.getSeconds();
  var min = today.getMilliseconds();
  date = year + "-" + zeroPadding(month,2) + "-" + zeroPadding(day,2);
  hours = hour + ":" + sec + ":" + min;
  return date;
}

// 0埋め関数
function zeroPadding(num,length){
    return ('0000000000' + num).slice(-length);
}