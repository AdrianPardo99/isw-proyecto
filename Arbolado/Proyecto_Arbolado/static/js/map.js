
function initMap() {

    navigator.geolocation.getCurrentPosition( function success(location){
        const latitude  = location.coords.latitude;
        const longitude = location.coords.longitude;
        /* Setting the user current location on the Map */
        const currentLocation = new google.maps.LatLng( latitude, longitude );
        /* Creating the map with the user current location */
        createMap( currentLocation );

    }, function( positionError ) {
        console.log(positionError['message']);
        /* If the user denied geolocation prompt - default to ESCOM IPN */
        const defaultLocation = new google.maps.LatLng(19.50467767240305, -99.14693541412099);
        /* Creating the map with the default location */
        createMap( defaultLocation );
    });
    
}

const createMap = ( location ) =>{
    
    const map = new google.maps.Map(document.getElementById('map'));
    const geocoder   = new google.maps.Geocoder();
    const infowindow = new google.maps.InfoWindow();

    map.setCenter( location );
    map.setZoom(18);
    /* Creating the Marker for the Map */
    const marker = new google.maps.Marker({
        map: map,
        draggable: true,
        animation: google.maps.Animation.DROP,
        position: map.getCenter(),
    });

    showInformation( map, marker, geocoder, infowindow );
    
    /* Adding the event to the marker */
    marker.addListener('dragend', () =>{
        showInformation( map, marker, geocoder, infowindow );
    });
}

const showInformation = ( map, marker, geocoder, infowindow ) => {
    
    let LatLng = marker.getPosition();
    const addressField = document.querySelector('#id_address'); 

    console.log(LatLng.lat());
    console.log(LatLng.lng());

    geocoder.geocode({ location: LatLng }, (results, status) => {
        if ( status == "OK") {
            if (results[0]) {
                let address = results[0].formatted_address;
                infowindow.setContent(address);
                infowindow.open(map, marker);
                /* Assigning the value to the addressField */
                addressField.value = address; 
            } 
            else {
                window.alert("No results found");
            }
        }
        else {
            window.alert("Geocoder failed due to: " + status);
        }
    }); 

}






