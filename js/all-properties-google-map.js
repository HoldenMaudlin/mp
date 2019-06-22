const $ = require('jQuery')

const markerColors = {
    'red': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
    'blue': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
    'yellow': 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
    'green': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
};

function getMarkerColor(prop_type) {
    if (prop_type == 'For Sale') return markerColors.red;
    if (prop_type == 'For Lease') return markerColors.blue;
    if (prop_type == 'Sold') return markerColors.yellow;
    if (prop_type == 'Leased') return markerColors.green;
}

function setMarkers(map, props) {
    var markers = []
    props.forEach(prop => {
        const coords = {
            lat: parseFloat(prop.latitude),
            lng: parseFloat(prop.longitude)
        };
        var marker = {
            position: coords,
            map: map,
            color: getMarkerColor(prop.type),
            key: prop.type,
            title: prop.address,
        };
        // Make marker responsive when clicked
        marker.addListener('click', function() {
            infowindow.open(map, marker);
        });
        // Make map repsonsive when clicked
        google.maps.event.addListener(marker, 'click', function(){
            infowindow.setContent(this.title);
            infowindow.open(map,this);
        });
        // Add marker to marker array to be used throughout script
        markers.push(marker);
    });
    return markers
};

function deleteMarkers(markers) {
    markers.forEach(mark => {
        mark.setMap(null);
    })
    return [];
}

function flipMarkers(markers, props, value) {
    // Passed in the new value of the checkbox
    // Call appropriate function to place or delete markers
    return value ? setMarkers(props) : deleteMarkers(markers);
}
 
function initMap(props) {
    // Callback for Google script
    var map;
    var markers = {};

    function displayProperties() {       
        map = new google.maps.Map(document.getElementById('map'), {
            center: latlng,
            zoom: 12
        });
        
        markers.sold = setMarkers(map, props.sold);
        markers.leased = setMarkers(map, props.leased);
        markers.for_sale = setMarkers(map, props.for_sale);
        markers.for_lease = setMarkers(map, props.for_lease);
    }

    // Add jQuery listeners here

    displayProperties();
}