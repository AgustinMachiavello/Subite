// Subite main javascript

const opts = {crossDomain: true};
var csrftoken = getCookie('csrftoken'); // token de sesión del usuario
// Token de la API de mapbox
var mapbox_token = "pk.eyJ1IjoiYWd1c3Rpbm1hY2hpYXZlbGxvIiwiYSI6ImNrMjNuZGkwYzAwZHQzZHMxM2xxbHJwbmoifQ.WZfyYnPjnCQJ6K4jFtXTJw"

// lleva un string al formato UTF8
function format_address_to_url(address){
  return address.split(' ').join('%20').split(',').join('%2C')
}

// lleva un string en formato UTF8 a normal
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

// Función para llamar a la url de registro de usuario
function subirme(id_ruta) {
  var domain = window.location.origin;
  var post_url = `${domain}/api/viajes/`;
  var post_data = {
    'ViajeRuta': id_ruta,
    'csrfmiddlewaretoken': csrftoken}
  var post_successful_url = `${domain}/viaje_success.html`;
  $.post(
    post_url,
    post_data,
    function(data) {
      window.location.replace(post_successful_url);
    }).fail(function(data) {
      alert("Algo salió mal :(");
    });
}

// Función para llamar a la url de registro de usuario
function signup(first_name, last_name, email, tel, password, birth) {
  var domain = window.location.origin;
  var post_url = `${domain}/api/test/`;
  var post_data = {
    'username': email,
    'first_name': first_name, 
    'last_name': last_name,
    'email': email,
    'Tel': tel,
    'password': password,
    'UsuFechNac': birth,
    'csrfmiddlewaretoken': csrftoken}
  var post_successful_url = `${domain}/index.html`;
  $.post(
    post_url,
    post_data,
    function(data) {
      window.location.replace(post_successful_url);
    }).fail(function(data) {
      alert("Not valid credentials");
    });
}

// Función para llamar a la url de inicio de sesión
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

// Dibuja la ruta sobre el mapa a partir de una lista de coordenadas
function add_route_layer(map, id, coordiantes, color){
  map.addLayer({
    "id": id.toString(),
    "type": "line",
    "source": {
    "type": "geojson",
    "data": {
    "type": "Feature",
    "properties": {},
    "geometry": {
    "type": "LineString",
    "coordinates": coordiantes,
  }
  }
  },
  "layout": {
    "visibility": 'visible',
    "line-join": "round",
    "line-cap": "round"
  },
  "paint": {

    "line-color": `#${color}`,
    "line-width": 8
  }
  });
}

// Dibuja un ícono en el mapa a traveś de sus coordenadas
function add_icon_layer(map, id, coordinates){
  map.loadImage('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Target_Corporation_logo_%28vector%29.svg/300px-Target_Corporation_logo_%28vector%29.svg.png', 
  function(error, image){
    if (error) throw error;
    map.addImage(id.toString(), image);
    map.addLayer({
      "id": id.toString(),
      "type": "symbol",
      "source": {
      "type": "geojson",
      "data": {
      "type": "FeatureCollection",
      "features": [{
      "type": "Feature",
      "geometry": {
      "type": "Point",
      "coordinates": coordinates,
      }
      }]
      }
      },"layout": {
        "visibility": 'visible',
        "icon-image": id.toString(),
        "icon-size": 0.1
      }
    });
    })
}


// Dibuja un mapa en pantalla a partir de sus coordenadas
function draw_route_map(center_coordinates, route_coordinates, icons_coordinates){

mapboxgl.accessToken = mapbox_token;
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11',
center: center_coordinates,
zoom: 15
});
var x = 0
var color = 888  // grey
map.on('load', function () {
  for (i in icons_coordinates){
    debugger;
    console.log("x:", x)
    add_icon_layer(map, x, icons_coordinates[i])
    x += 1
  }
  for (i in route_coordinates){
    console.log("Route:", route_coordinates[i])
    add_route_layer(map, x, route_coordinates[i], color)
    console.log("x:", x)
    console.log("color:", color)
    color += 100
    x += 1
  }
});
}