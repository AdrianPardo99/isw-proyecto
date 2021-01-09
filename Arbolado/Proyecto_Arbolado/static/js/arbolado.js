/* Module Pattern */

/* Función de flecha anónima auto-invocada */
const myModule = (() => {
    'use strict'
    /* Private Stuff */
    let trees_id   = [];
    
    const formSolicitud = document.querySelector('#formSolicitud');
    const formTree      = document.querySelector('#formTree');
    const treeURL       = 'http://127.0.0.1:8000/arbolado/register/tree';
    const formSection   = document.querySelector('#formSection');
    const sectURL       = 'http://127.0.0.1:8000/arbolado/register/section';
    const tableBody     = document.querySelector('#tbodyTable');

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
            
            $.ajax({
                type: 'POST',
                url : sectURL,
                data: formData,
                success: function( response ){
                    let section_id = response['id'];
                    /* Calling the function for register the solicitud */
                    registerSolicitud( section_id );
                    /* Reset the form fields with jQuery function */
                    $('#formSection')[0].reset();
                    $('#formSolicitud')[0].reset();
                },
                error: function( error ){
                    console.log( error );
                },
                cache: false,
                contentType: false,
                processData: false,
            })
        }
    }

    const registerSolicitud = ( section_id ) => {
        const formData = new FormData( formSolicitud );
        formData.append('section', section_id);
        $.ajax({
            type: 'POST',
            url : '',
            data: formData,
            success: function( response ){
                console.log( response );
            },
            error: function( error ){
                console.log( error );
            },
            cache: false,
            contentType: false,
            processData: false,
        }) 
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
                /* Adding the id of the tree */
                trees_id.push( response['id'] );
            },
            error: function( error ){
                console.log( error )
            },
            cache: false,
            contentType: false,
            processData: false,
        })
    }

    const addTableRow = (response) =>{
        const description  = response['description'].substring( 0, 15) + '...'; 
        const tr = document.createElement('tr');
        const deleteImage = document.createElement('img');
        const td          = document.createElement('td');
        /* Setting up image properties */
        deleteImage.src    = 'http://127.0.0.1:8000/static/img/delete.png';
        deleteImage.id     = 'btnDeleteTree';
        deleteImage.height = 25;
        deleteImage.width  = 25;
        td.append( deleteImage );

        tr.innerHTML = `
        <td> ${response['name']}    </td>
        <td> ${response['species']} </td>
        <td> ${description}         </td>
        <td> ${response['status']}  </td>
        <td> ${response['amount']}  </td>`
        tr.append(td);
        /* Adding the rows for the table */
        tableBody.append(tr);
    }

    /* Public Functions */
    return {
        newTree:    registerTree,
        newSection: registerSection,
    };

})();
