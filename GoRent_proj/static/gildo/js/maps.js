var latitude = 10.3157
var longitude = 123.8854
var zoom_level = 10
// function initMap() {
//     const cebu = {lat: 10.3157, lng: 123.8854};
//     const map = new google.maps.Map(document.getElementById("map"), {
//         zoom: 4,
//         center: cebu,
//     });
//     new google.maps.Marker({
//         position: cebu,
//         map,
//         title: "Hello World!",
//     });
// }

// MAP CODE
// map = L.map('map1').setView([latitude, longitude], zoom_level); // ([LONG, LAT], ZOOM-LEVEL)
map = L.map('map', {
  center: [latitude, longitude],
  zoom: zoom_level,
  zoomControl: false,
});

// LAYER CODE (MURAG NI KATUNG SATELITE, ROAD, ETC. SA GOOGLE)
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYmxhY2tsaXN0NjI2OTkiLCJhIjoiY2txZ2ZvY3llMDRqdjJwbnk0cW8xZHRwbiJ9.pEY5vLDBVfKplzQe92sMMw', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYmxhY2tsaXN0NjI2OTkiLCJhIjoiY2txZ2ZvY3llMDRqdjJwbnk0cW8xZHRwbiJ9.pEY5vLDBVfKplzQe92sMMw'
}).addTo(map);

// MARKER CODE
markers.forEach(marker => {
  marker.addTo(map)
});

// GEOSEARCH
geocoder = L.Control.Geocoder.nominatim()
geosearch_control = L.Control.geocoder({
  defaultMarkGeocode: false,
  collapsed: false,
  position: "topleft",
  suggestTimeout: 100,
  geocoder: geocoder,
}).addTo(map);

var search_boundingbox
geosearch_control.on('markgeocode', function(e) { // BOUNDING-BOX
  var bbox = e.geocode.bbox;
  console.log(bbox);

  if (search_boundingbox != null) {
    search_boundingbox.remove()
    search_boundingbox = L.polygon([
      bbox.getSouthEast(),
      bbox.getNorthEast(),
      bbox.getNorthWest(),
      bbox.getSouthWest()
    ]).addTo(map);
    map.fitBounds(search_boundingbox.getBounds());
  }
  else {
    search_boundingbox = L.polygon([
      bbox.getSouthEast(),
      bbox.getNorthEast(),
      bbox.getNorthWest(),
      bbox.getSouthWest()
    ]).addTo(map);
    map.fitBounds(search_boundingbox.getBounds());
  }

  console.log(e);
  if (user_flag == false) {
    addPopupFromResult(map, e.geocode.center, e.geocode)
    user_locate.location = e.geocode.center
    user_locate.address = e.geocode.name
  }
});

map.on('click', function(e) { // DISPLAY LOCATION ON CLICK
  if (user_locate.isLocating) {
    geocoder.reverse(e.latlng, map.options.crs.scale(map.getZoom()), function(results) {
      result = results[0]; // THE "result" VARIABLE IS A geocode OBJECT
      addPopupFromResult(map, e.latlng, result)
      
      user_locate.location = e.latlng
      user_locate.address = result.name
      toggleMapLocate()
      
      console.log(geolocate_marker.getLatLng())
    });
  }
});


function showLocation(position) {
  position = L.latLng([position.coords.latitude, position.coords.longitude])
  map.setView(position, 15)
  geocoder.reverse(position, map.options.crs.scale(map.getZoom()), function(results) {
    result = results[0]; // THE "result" VARIABLE IS A geocode OBJECT
    addPopupFromResult(map, position, result, "You are here: <br>")

    user_locate.location = position
    user_locate.address = result.name

    console.log(geolocate_marker.getLatLng())
  });
}

var geolocate_marker;
function addPopupFromResult(map, latlng, result="", message="") { // DISPLAY LOCATION ON CLICK
  if (result != null) {
    if (geolocate_marker != null) {
      geolocate_marker
        .setLatLng(latlng)
        .setPopupContent(message +(result.html || result.name))
        .openPopup();
    } else {
      geolocate_marker = L.marker(latlng)
        .bindPopup(message +result.name)
        .addTo(map)
        .openPopup();
    }
  }
}




// searchControl = new  GeoSearch.GeoSearchControl({
//   provider: new  GeoSearch.OpenStreetMapProvider(),
//   style: 'bar',
//   // showMarker: true,
//   // autoClose: true,
//   // updateMap: true,
// });

// map.addControl(searchControl);


// const provider = new GeoSearch.OpenStreetMapProvider();
// const results = provider.search({ query: "spain" });
// console.log(results);

// const search = new GeoSearch.GeoSearchControl({
//   provider: new GeoSearch.OpenStreetMapProvider(),
// });
// map.addControl(search);



// const searchControl = new GeoSearchControl({
//   provider: new OpenStreetMapProvider(),
// });
// map.addControl(searchControl);