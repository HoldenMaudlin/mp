const markerColors = {
    'red': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
    'blue': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
    'yellow': 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
    'green': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
};

function setMarkers(map, infowindow, props, marker_color) {
    var markers = [];
    props.forEach(prop => {
        const coords = {
            lat: parseFloat(prop.lat),
            lng: parseFloat(prop.lng)
        };
        var marker =  new google.maps.Marker({
            position: coords,
            map: map,
            icon: marker_color,
            key: prop.type,
            title: prop.address,
        });
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
    return markers;
};

function deleteMarkers(markers) {
    markers.forEach(mark => {
        mark.setMap(null);
    })
    return [];
}

function flipMarkers(map, infowindow, markers, props, icon, value) {
    // Passed in the new value of the checkbox
    // Call appropriate function to place or delete markers
    return value ? setMarkers(map, infowindow, props, icon) : deleteMarkers(markers);
}
 
function displayProperties(props) {
    // Callback for Google script
    var map;
    var infowindow = new google.maps.InfoWindow();
    var markers = {};
    const latlng = {lat: 34.023535, lng: -118.3973563};
    map = new google.maps.Map(document.getElementById('map'), {
        center: latlng,
        zoom: 12
    });
    
    // Add initial markers
    markers.sold = setMarkers(map, infowindow, props.sold, markerColors.red);
    markers.leased = setMarkers(map, infowindow, props.leased, markerColors.blue);
    markers.for_sale = setMarkers(map, infowindow, props.for_sale, markerColors.green);
    markers.for_lease = setMarkers(map, infowindow, props.for_lease, markerColors.yellow);
    
    // jQuery listners
    $('#for_sale').click(function() {
        const val = $(this).attr("checked") !== "checked";
        $(this).attr("checked", val);
        markers.for_sale = flipMarkers(map, infowindow, markers.for_sale, props.for_sale, markerColors.green, val)
    });

    $('#for_lease').click(function() {
        const val = $(this).attr("checked") !== "checked";
        $(this).attr("checked", val);
        markers.for_lease = flipMarkers(map, infowindow, markers.for_lease, props.for_lease, markerColors.yellow, val)
    });

    $('#sold').click(function() {
        const val = $(this).attr("checked") !== "checked";
        $(this).attr("checked", val);
        markers.sold = flipMarkers(map, infowindow, markers.sold, props.sold, markerColors.red, val)
    });

    $('#leased').click(function() {
        const val = $(this).attr("checked") !== "checked";
        $(this).attr("checked", val);
        markers.leased = flipMarkers(map, infowindow, markers.leased, props.leased, markerColors.blue, val)
    });
}