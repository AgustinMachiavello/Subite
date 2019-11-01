// Subite main javascript

const opts = {crossDomain: true};
var csrftoken = getCookie('csrftoken');
var mapbox_token = "pk.eyJ1IjoiYWd1c3Rpbm1hY2hpYXZlbGxvIiwiYSI6ImNrMjNuZGkwYzAwZHQzZHMxM2xxbHJwbmoifQ.WZfyYnPjnCQJ6K4jFtXTJw"




function format_address_to_url(address){
  return address.split(' ').join('%20').split(',').join('%2C')
}

function unformat_url_to_address(address){
  return address.split('%20').join(' ').split('%2C').join(',')
}

// returns browser cookie containing user data and other relevant information
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

// login request
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

// return the url parameters
function getUrlVars() {
  // Gets called like this: var fType = getUrlVars()["type"];
  var vars = {};
  var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi,    
  function(m,key,value) {
    vars[key] = value;
  });
  return vars;
}

// draw a map with a route and an icon
function draw_route_map(center_coordinates, route_coordinates, icons_coordinates){
mapboxgl.accessToken = mapbox_token;
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11',
center: center_coordinates,
zoom: 15
});
map.on('load', function () {
  debugger;
  for (a in icons_coordinates){
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
      "coordinates": icons_coordinates[a],
    }
  }]
}
},"layout": {
  "icon-image": "point",
  "icon-size": 0.03
}
});
})
}//end if 'if (icons_array != null)'

  for (i in route_coordinates){
    debugger;
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
      "coordinates": route_coordinates[i],
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
}
});
}