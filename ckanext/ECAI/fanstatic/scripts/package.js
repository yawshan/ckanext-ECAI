//add map
if($('#map').length){

	var map = L.map('map').setView([0, 0], 1);
	//initialize MapQuestLayer
	MapQuestOpen_OSM = L.tileLayer('http://otile{s}.mqcdn.com/tiles/1.0.0/{type}/{z}/{x}/{y}.{ext}', {
		type: 'map',
		ext: 'jpg',
		attribution: 'Tiles Courtesy of <a href="http://www.mapquest.com/">MapQuest</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
		subdomains: '1234'
	}).addTo(map);
	//initialize draw layer
	var drawnItems = new L.FeatureGroup();
	map.addLayer(drawnItems);
	//initialize Draw Feature Control
	var drawControl = new L.Control.Draw({
		draw: {
			polygon: true,
			polyline: false,
			rectangle: true,
			circle: false,
			marker: true
		},
		edit: {
			featureGroup: drawnItems,
			remove: false
		}
	});
	map.addControl(drawControl);
	//eventListener draw-create
	map.on('draw:created', function (e) {
		document.getElementById("field-spatial").value=JSON.stringify(e.layer.toGeoJSON().geometry)
		drawnItems.clearLayers();
		drawnItems.addLayer(e.layer);
	});
	//eventListener draw-edited
	map.on('draw:edited',function (e) {
		e.layers.eachLayer(function (layer) {
			document.getElementById("field-spatial").value=JSON.stringify(layer.toGeoJSON().geometry)
			drawnItems.clearLayers();
			drawnItems.addLayer(layer);
	    	});
	});

	if (document.getElementById("field-spatial").value != '') {
	  var geojson = JSON.parse(document.getElementById("field-spatial").value);
	  var extentLayer = L.geoJson(geojson, {style: function (feature) {
	    return {color: feature.properties.color};
	  }}).addTo(map);
	  if (geojson.type == 'Point') {
	    map.setView(L.latLng(geojson.coordinates[1], geojson.coordinates[0]), 9);
	  } else {
	    map.fitBounds(extentLayer.getBounds());
	  }
	}
}
$("fieldset fieldset legend").siblings().slideToggle();
$('#spatialcontent').hide();

$(document).ready(function(){
  $('fieldset fieldset legend').click(function(){
   $(this).siblings().slideToggle("fast");
  });

  $('#showspatial').click(function(){
     if($('#showspatial').text()=='Show more'){
	$('#showspatial').text('Show less');
     }else{
	$('#showspatial').text('Show more');
     }
     $('#spatialcontent').toggle();
  });
});




