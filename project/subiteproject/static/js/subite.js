// Subite main javascript

const opts = {crossDomain: true};
var login_form = document.getElementById('login-form');

$('#signin-form').submit(function(e){
    e.preventDefault();
    var email = document.getElementById("inputEmail").value;
    var password = document.getElementById("inputPassword").value;
    login(email, password);
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function login(email, password) {
  submitOK = "true";
  var at = email.indexOf("@");

  if (at == -1) {
    alert("Not a valid e-mail!");
    submitOK = "false";
  }

  if (submitOK === "true") {
    var domain = window.location.origin;
    var post_url = `${domain}/api/users/signin/`;
    var post_data = {'username': email, 'password': password, 'csrfmiddlewaretoken': csrftoken}
    var post_successful_url = `${domain}/index.html`;
    console.log(post_url)
    $.post(
      post_url,
      post_data,
      function(data) {
        window.location.replace(post_successful_url);
      }).fail(function() {
        alert("Not valid credentials");
      });
  }
}