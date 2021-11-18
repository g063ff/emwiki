
/* eslint-disable */
// Disable ESLint because this file will be deleted recentlly
const context = JSON.parse(document.getElementById('context').textContent);
$(document).ready(function() {
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie != '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie('csrftoken');
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type)) {
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
      }
    },
  });
});


$(function() {
  $('.button_url').on('click', function() {
    const db_id = $(this).attr('name');
    $.ajax({
      url: context['search_uri'],
      type: 'post',
      data: {'button_type': 'url', 'id': db_id},
      dataType: 'json',
    })
        .done(function() {
        })
        .fail(function() {
        });
    // クッキーにArticle名を保存すると, Articleアプリを開いたときロードされる
    Cookies.set('next-link', $(this).attr('data-href'));
    return window.open(context['article_base_uri'], '_blank').focus();
  });
});

$(function() {
  $('.button_fav').on('click', function() {
    const db_id = $(this).attr('name');
    $.ajax({
      url: context['search_uri'],
      type: 'post',
      data: {'button_type': 'fav', 'id': db_id},
      dataType: 'json',
    })
        .done(function(res) {
          const name = res['id'];
          $('.button_fav[name=' + name+ ']').toggleClass('active');
        })
        .fail(function() {
        });
  });
});
