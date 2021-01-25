/* Module Pattern */

/* Función de flecha anónima auto-invocada */
const myModule = (() => {
    'use strict'
    /* Private Stuff */
    let trees_id   = [];
    let lat, lng;
    
    const csrf          = document.getElementsByName('csrfmiddlewaretoken');
    const alertBox      = document.querySelector('#alert-box');
    const tableTree     = document.querySelector('#tableTree');
    const tableBody     = document.querySelector('#tbodyTable');
    const addressField  = document.querySelector('#id_address');
    /* HTML FORMS*/
    const formSolicitud = document.querySelector('#formSolicitud');
    const formTree      = document.querySelector('#formTree');
    const formSection   = document.querySelector('#formSection');
    const formReport    = document.querySelector('#formReport');
    /* DJANGO URLS */
    const mainURL       = 'http://127.0.0.1:8000/';
    const treeURL       = 'http://127.0.0.1:8000/arbolado/register/tree';
    const sectURL       = 'http://127.0.0.1:8000/arbolado/register/section';

    const handleAlerts = (type, title, text) =>{
        alertBox.innerHTML = 
        `<div class="cell callout ${type}" role="alert">
            <h5> ${title} </h5>
            <p>  ${text}  </p>    
        </div>`;
    }

    const registerReport = () =>{
        console.log('Entre aquí después del submit');
        const formData = new FormData( formReport );
        formData.append('address', addressField.value);

        $.ajax({
            type: 'POST',
            url : '', /* Blank means the current url */
            enctype: 'multipart/form-data',
            data: formData,
            success: function( response ){
                console.log('Respuesta del Registro del Reporte: ', response );
                /* Showing the Alert Message to the user */
                handleAlerts(
                    'success', 
                    '¡Tú reporte ha sido enviado con éxito! ', 
                    'Revisa tú correo electrónico para ver el código de tu reporte y así darle seguimiento.'
                );
                
                setTimeout(()=>{
                    /* Reset the form fields with jQuery function */
                    $('#formReport')[0].reset();
                    alertBox.innerHTML = "";
                    /* HTTP redirect with window.location.replace -> Go to 'Main Page' */ 
                    window.location.replace( mainURL );
                }, 5000)

            },
            error: function( error ){
                console.log( error );
            },
            cache: false,
            contentType: false,
            processData: false,

        })
        

    }

    const registerSolicitud = ( section_id ) => {
        const formData = new FormData( formSolicitud );
        formData.append('section', section_id);
        $.ajax({
            type: 'POST',
            url : '', /* Blank means the current url */
            data: formData,
            success: function( response ){
                console.log('Respuesta del Registro de la Solicitud: ', response );
                tableBody.innerHTML = "";
                /* Showing the Alert Message to the user */
                handleAlerts(
                    'success', 
                    '¡Tú solicitud ha sido enviada con éxito! ', 
                    'Revisa tú correo electrónico para ver el código de tu solicitud y así darle seguimiento.'
                );
                
                setTimeout(()=>{
                    /* Reset the form fields with jQuery function */
                    $('#formSection')[0].reset();
                    $('#formSolicitud')[0].reset();
                    alertBox.innerHTML = "";
                    /* HTTP redirect with window.location.replace -> Go to 'Main Page' */ 
                    window.location.replace( mainURL );
                }, 5000)
                
            },
            error: function( error ){
                console.log( error );
            },
            cache: false,
            contentType: false,
            processData: false,
        }) 
    }
    
    const registerSection = () => {
        /* Validar los campos */
        if ( trees_id.length == 0){
            alert('¡Debes ingresar al menos un árbol para enviar la solicitud!');
        }
        else{
            const formData = new FormData( formSection ); 
            for( let id of trees_id ){
                formData.append('trees', id);
            }
            /* Each field of formData is a list, ['element1', 'element2']*/
            formData.append('address', addressField.value);
            formData.append('coords', lat+','+lng);
            $.ajax({
                type: 'POST',
                url : sectURL,
                enctype: 'multipart/form-data', /* Enctype for images and other kind of media files */
                data: formData,
                success: function( response ){
                    console.log( response );
                    let section_id = response['id'];
                    console.log('Identificador Sección: ', section_id);
                    /* Calling the function for register the solicitud */
                    registerSolicitud( section_id );   
                },
                error: function( error ){
                    console.log( error );
                    handleAlerts(
                        'alert', 
                        'La solicitud no fue enviada al Servidor', 
                        'Algunos datos están incompletos o no cumplen el formato establecido'
                    );
                },
                cache: false,
                contentType: false,
                processData: false,
            })
        }
    }

    const deleteTree = ( id_row, id_tree ) => {
        console.log('Fila Tabla', id_row);
        console.log('Indice Arbol', id_tree);
        const formData = new FormData();
        formData.append('csrfmiddlewaretoken', csrf[0].value);
        formData.append('id_tree', id_tree);
        /* Deleting the Tree from the Tree Model of the Database using an AJAX Request*/
        $.ajax({
            type: 'POST',
            url : `http://127.0.0.1:8000/arbolado/delete/tree`,
            data: formData,
            success: function( response ){
                console.log( response );  
            },
            error: function( error ){
                console.log( error );
                console.log('No hubo respuesta del Servidor');
            },
            cache: false,
            contentType: false,
            processData: false,
        })
        /* Deleting the current tree from the trees array */
        /* Position, Number of elements that will be removing starting at 'position' */
        const deletedTree = trees_id.splice(id_row-1, 1);
        console.log('Elemento Eliminado:', deletedTree);
        console.log('Arreglo de Árboles después de eliminar', trees_id );
        /* Deleting the current row from the table */
        tableTree.deleteRow( id_row );
    }

    const registerTree = () => {
        const formData = new FormData( formTree );
        $.ajax({
            type: 'POST',
            url : treeURL,
            enctype: 'multipart/form-data', /* Enctype for images and other kind of media files */
            data: formData,
            success: function( response ){
                console.log( response );
                /* Adding the rows int the table */
                addTableRow( response );
                /* Reset the form fields with jQuery function */
                $('#formTree')[0].reset();
            },
            error: function( error ){
                console.log( error );
                alert('¡Faltan campos por llenar!');
            },
            cache: false,
            contentType: false,
            processData: false,
        })
    }

    const addTableRow = ( response ) =>{
        const tree_id = response['id'];
        const description  = response['description'].substring(0, 15) + '...'; 
        const tr = document.createElement('tr');
        const td          = document.createElement('td');
        /* Setting up image properties */
        td.innerHTML =
        ` <img src="http://127.0.0.1:8000/static/img/delete.png" id="${tree_id}" height="25" width="25" onclick="deleteRow(this)">
          </img> `;

        tr.innerHTML = `
        <td class="text-format"> ${response['species']} </td>
        <td class="text-format"> ${description}         </td>
        <td class="text-format"> ${response['status']}  </td>
        <td class="text-format"> ${response['amount']}  </td>`;
        tr.append(td);
        /* Adding the rows for the table */
        tableBody.append(tr);
        /* Adding the id of the tree in the trees ids list */
        trees_id.push( tree_id );
        console.log('Arreglo de Árboles', trees_id );
    }

    /* GOOGLE MAPS JAVASCRIPT API*/

    const initMap = () => {

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
    
        lat = LatLng.lat();
        lng = LatLng.lng();
    
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

    
    /* Public Functions */
    return {
        newTree:    registerTree,
        newSection: registerSection,
        newReport: registerReport,
        deleteTree: deleteTree,
        mapFunct:   initMap,
    };

})();
