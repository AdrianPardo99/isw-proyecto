/* Module Pattern */

/* Función de flecha anónima auto-invocada */
const myModule = (() => {
    'use strict'
    /* Private Stuff */
    let trees_id   = [];
    
    const csrf          = document.getElementsByName('csrfmiddlewaretoken');
    const alertBox      = document.querySelector('#alert-box');
    const mainURL       = 'http://127.0.0.1:8000/';
    const tableTree     = document.querySelector('#tableTree');
    const formSolicitud = document.querySelector('#formSolicitud');
    const formTree      = document.querySelector('#formTree');
    const treeURL       = 'http://127.0.0.1:8000/arbolado/register/tree';
    const formSection   = document.querySelector('#formSection');
    const sectURL       = 'http://127.0.0.1:8000/arbolado/register/section';
    const tableBody     = document.querySelector('#tbodyTable');

    const handleAlerts = (type, title, text) =>{
        alertBox.innerHTML = 
        `<div class="cell callout ${type}" role="alert">
            <h5> ${title} </h5>
            <p>  ${text}  </p>    
        </div>`;
    }

    const registerSolicitud = ( section_id ) => {
        const formData = new FormData( formSolicitud );
        formData.append('section', section_id);
        $.ajax({
            type: 'POST',
            url : '',
            data: formData,
            success: function( response ){
                console.log('Respuesta Solicitud: ', response );
                tableBody.innerHTML = "";
                /* Showing the Alert Message to the user */
                handleAlerts(
                    'success', 
                    '¡Tú solicitud se envió con éxito! ', 
                    'Revisa tú correo electrónico para ver el código de tu solicitud y así darle seguimiento.'
                );
                
                setTimeout(()=>{
                    /* Reset the form fields with jQuery function */
                    $('#formSection')[0].reset();
                    $('#formSolicitud')[0].reset();
                    alertBox.innerHTML = "";
                    /* HTTP redirect with window.location.replace */ 
                    window.location.replace( mainURL );
                }, 4000)
                
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
            
            $.ajax({
                type: 'POST',
                url : sectURL,
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
        <td> ${response['species']} </td>
        <td> ${description}         </td>
        <td> ${response['status']}  </td>
        <td> ${response['amount']}  </td>`;
        tr.append(td);
        /* Adding the rows for the table */
        tableBody.append(tr);
        /* Adding the id of the tree in the trees ids list */
        trees_id.push( tree_id );
        console.log('Arreglo de Árboles', trees_id );
    }

    
    /* Public Functions */
    return {
        newTree:    registerTree,
        newSection: registerSection,
        deleteTree: deleteTree,
    };

})();
