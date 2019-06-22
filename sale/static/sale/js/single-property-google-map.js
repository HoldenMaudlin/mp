function displayProperty(latlng, title) {  
    // Google Map Instance
    var map;   
    var infowindow = new google.maps.InfoWindow();

    // Callback for Google script
    map = new google.maps.Map(document.getElementById('map'), {
        center: latlng,
        zoom: 14
    });
    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        title: title
    })
    google.maps.event.addListener(marker, 'click', function(){
        infowindow.setContent(this.title);
        infowindow.open(map,this);
    })
    marker.addListener('click', function() {
        infowindow.open(map, marker);
    });

}