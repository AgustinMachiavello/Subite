// Subite main javascript

const opts = {crossDomain: true};

$('#signin-form').submit(function(e){
    e.preventDefault();
    var email = document.getElementById("inputEmail").value;
    var password = document.getElementById("inputPassword").value;
    login(email, password);
});

$('#new-route-form').submit(function(e){
  e.preventDefault();
  var from = document.getElementById("from").value;
  var to = document.getElementById("to").value;
  get_coordinates(from)
  debugger;
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
var mapbox_token = 'pk.eyJ1IjoiYWd1c3Rpbm1hY2hpYXZlbGxvIiwiYSI6ImNrMjNuZGkwYzAwZHQzZHMxM2xxbHJwbmoifQ.WZfyYnPjnCQJ6K4jFtXTJw'
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

function get_coordinates(direction){
  var formated_direction = direction.split(' ').join('%20')
  formated_direction.split(' ').join('%2C')
  debugger;
  var post_data = {}
  var post_url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${formated_direction}.json?limit1&access_token=${mapbox_token}`
  var post_successful_url = ''
  $.get(
    post_url,
    post_data,
    function(data) {
      console.log(data)
    }).fail(function() {
      alert("Algo salió mal");
    });
}