// Subite main javascript

const opts = {crossDomain: true};
var csrftoken = getCookie('csrftoken');
var mapbox_token = "pk.eyJ1IjoiYWd1c3Rpbm1hY2hpYXZlbGxvIiwiYSI6ImNrMjNuZGkwYzAwZHQzZHMxM2xxbHJwbmoifQ.WZfyYnPjnCQJ6K4jFtXTJw"
var openroute_token = "5b3ce3597851110001cf6248db84a52feecd456dbb2a4ee52a35ee4f"

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
  var formated_from = from.split(' ').join('%20')
  formated_from = formated_from.split(',').join('%2C')
  var formated_to = to.split(' ').join('%20')
  formated_to = formated_to.split(',').join('%2C')
  var domain = window.location.origin;
  window.location.href = `${domain}/select_route/?from=${formated_from}&to=${formated_to}`;
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
  formated_direction = formated_direction.split(',').join('%2C')
  var post_data = {'format': 'json'}
  var post_url = `https://nominatim.openstreetmap.org/search?q=${formated_direction}&format=json`
  var output = null
  $.ajax({
    type: 'POST',
    url: post_url,
    data: post_data,
    success: function(result){
      output = result
    },
    dataType: 'json',
    async:false
  });
  return output
}

function getUrlVars() {
  // Gets called like this: var fType = getUrlVars()["type"];
  var vars = {};
  var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi,    
  function(m,key,value) {
    vars[key] = value;
  });
  return vars;
}

function visualize_route(){
  var from = document.getElementById("from").value;
  var to = document.getElementById("to").value;
  var formated_from = from.split(' ').join('%20')
  formated_from = formated_from.split(',').join('%2C')
  var formated_to = to.split(' ').join('%20')
  formated_to = formated_to.split(',').join('%2C')
  var domain = window.location.origin;
  var open_url = `${domain}/preview_route?from=${formated_from}&to=${formated_to}`;
  console.log(open_url)
  window.open(open_url, '_blank');
}

function get_route(coo_from_lat, coo_from_lon, coo_to_lat, coo_to_lon){
  // NOT VALID FOR URUGUAY var get_url = `https://api.mapbox.com/directions/v5/mapbox/walking/${coo_from_lon},${coo_from_lat};${coo_to_lon},${coo_to_lat}?access_token=${mapbox_token}`
  var get_url = `https://api.openrouteservice.org/v2/directions/driving-car?api_key=${openroute_token}&start=${coo_from_lon},${coo_from_lat}&end=${coo_to_lon},${coo_to_lat}`
  var get_data = {}
  var output = null
  console.log(get_url)
  $.ajax({
    type: 'GET',
    url: get_url,
    data: get_data,
    success: function(result){
      output = result
    },
    error:function(result){
      console.log("Algo salió mal en get_route")
    },
    dataType: 'json',
    async:false
  });
  return output
}

function visualize_map(center_array, coordinates_array, icon_array){
mapboxgl.accessToken = 'pk.eyJ1IjoiYWd1c3Rpbm1hY2hpYXZlbGxvIiwiYSI6ImNrMjNuZGkwYzAwZHQzZHMxM2xxbHJwbmoifQ.WZfyYnPjnCQJ6K4jFtXTJw';
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11',
center: center_array,
zoom: 15
});
 
map.on('load', function () {
  if (icon_array != null){
    map.loadImage('http://cdn.onlinewebfonts.com/svg/img_527461.png', 
    function(error, image){
      if (error) throw error;
      map.addImage('point', image);
      map.addLayer({
        "id": "points",
        "type": "symbol",
        "source": {
        "type": "geojson",
        "data": {
        "type": "FeatureCollection",
        "features": [{
        "type": "Feature",
        "geometry": {
        "type": "Point",
        "coordinates": icon_array,
        }
        }]
        }
        },"layout": {
          "icon-image": "point",
          "icon-size": 0.03
          }
          });
    })
  }

map.addLayer({
"id": "route",
"type": "line",
"source": {
"type": "geojson",
"data": {
"type": "Feature",
"properties": {},
"geometry": {
"type": "LineString",
"coordinates": coordinates_array,
}
}
},
"layout": {
"line-join": "round",
"line-cap": "round"
},
"paint": {
"line-color": "#888",
"line-width": 8
}
});
});
}