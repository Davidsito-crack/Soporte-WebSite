// Función para validar el documento al subir
function validarDocumento(event) {
    event.preventDefault();  // Evita el envío automático del formulario

    var archivo = document.getElementById('comodato');
    if (archivo.files.length === 0) {
        Swal.fire({
            icon: 'info',
            title: '¡Atención!',
            text: 'Por favor, selecciona un documento para subir.',
            toast: true,
            position: 'center',
            timer: 3000,
            timerProgressBar: true,
            showConfirmButton: false,
            customClass: {
                container: 'swal-toast-container'
            }
        });
        return false;
    }

    Swal.fire({
        title: '¡Subir documento!',
        text: 'Introduce la contraseña de administrador para confirmar la subida',
        icon: 'info',
        input: 'password',
        inputLabel: 'Contraseña de administrador',
        inputPlaceholder: 'Contraseña',
        inputAttributes: {
            maxlength: 20,
            autocapitalize: 'off',
            autocorrect: 'off'
        },
        showCancelButton: true,
        confirmButtonText: 'Subir',
        cancelButtonText: 'Cancelar',
        customClass: {
            confirmButton: 'btn btn-primary',
            cancelButton: 'btn btn-secondary',
            title: 'text-primary',
            input: 'form-control',
            container: 'swal2-info'
        },
        buttonsStyling: false,
        preConfirm: (password) => {
            return new Promise((resolve) => {
                // Simular una verificación de contraseña de administrador
                setTimeout(() => {
                    if (password === '1234') {  // Reemplaza '1234' con la contraseña real
                        resolve();
                    } else {
                        Swal.showValidationMessage('Contraseña incorrecta');
                    }
                }, 1000);
            });
        }
    }).then((result) => {
        if (result.isConfirmed) {
            // Mostrar animación de carga antes de enviar el formulario
            mostrarAnimacionCarga();
            document.getElementById('upload-form').submit();  // Envía el formulario para subir el documento
        }
    });
}

// Función para confirmar la eliminación del documento con contraseña de administrador
function confirmarEliminacion(event, formId) {
    event.preventDefault();  // Evita el envío automático del formulario

    Swal.fire({
        title: '¡WARNING!',
        text: '¿Estás seguro de que deseas eliminar este documento?',
        icon: 'warning',
        input: 'password',
        inputLabel: 'Introduce la contraseña de administrador',
        inputPlaceholder: 'Contraseña',
        inputAttributes: {
            maxlength: 20,
            autocapitalize: 'off',
            autocorrect: 'off'
        },
        showCancelButton: true,
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        customClass: {
            confirmButton: 'btn btn-danger',
            cancelButton: 'btn btn-secondary',
            title: 'text-danger',
            input: 'form-control',
            container: 'swal2-warning'
        },
        buttonsStyling: false,
        preConfirm: (password) => {
            return new Promise((resolve) => {
                setTimeout(() => {
                    if (password === '1234') {  // Reemplaza '1234' con la contraseña real
                        resolve();
                    } else {
                        Swal.showValidationMessage('Contraseña incorrecta');
                    }
                }, 1000);
            });
        }
    }).then((result) => {
        if (result.isConfirmed) {
            document.getElementById(formId).submit();  // Envía el formulario para eliminar el documento
        }
    });
}

// Función para mostrar la animación de carga
function mostrarAnimacionCarga() {
    var animacionCarga = document.getElementById('loading-animation');
    animacionCarga.style.display = 'block';
}

// Función para ocultar la animación de carga
function ocultarAnimacionCarga() {
    var animacionCarga = document.getElementById('loading-animation');
    animacionCarga.style.display = 'none';
}

// Asignar la función confirmarEliminacion a los botones de eliminar
document.addEventListener('DOMContentLoaded', function() {
    // Asignar la función confirmarEliminacion a los botones de eliminar
    const deleteButtons = document.querySelectorAll('.ELIMINAR');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.stopPropagation(); // Evita que el clic se propague al contenedor de la tarjeta
            const formId = this.closest('form').id;
            confirmarEliminacion(event, formId);
        });
    });

    // Asignar la función validarDocumento al botón de subir
    const uploadButton = document.querySelector('button[type="submit"]');
    uploadButton.addEventListener('click', function(event) {
        event.stopPropagation(); // Evita que el clic se propague al contenedor de la tarjeta
        validarDocumento(event);
    });

    // Asignar la función para evitar la rotación al botón de descargar
    const downloadButtons = document.querySelectorAll('.DESCARGA');
    downloadButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.stopPropagation(); // Evita que el clic se propague al contenedor de la tarjeta
        });
    });

    // Ocultar la animación de carga al cargar la página
    ocultarAnimacionCarga();
});

function rotateCard(element) {
    element.classList.toggle('rotated');
}

document.addEventListener("DOMContentLoaded", function() {
    // Función para manejar la carga de la imagen
    document.querySelectorAll('.card-back').forEach(function(cardBack) {
        var employeeImage = cardBack.querySelector('img.foto-atras');
        var backupImage = cardBack.querySelector('img[alt="Imagen de respaldo"]');

        var img = new Image();
        img.src = employeeImage.src;
        img.onload = function() {
            console.log('Imagen cargada: ' + employeeImage.src); // Para depuración
        };
        img.onerror = function() {
            console.log('Imagen no cargada: ' + employeeImage.src); // Para depuración
            // Imagen no cargada, mostrar imagen de respaldo
            employeeImage.style.display = 'none';
            backupImage.style.display = 'block';
        };
    });
});
// Función para solicitar la contraseña antes de descargar
function solicitarContrasena(url) {
    Swal.fire({
        title: 'Contraseña requerida',
        text: 'La contraseña es el permiso para realizar la descarga',
        icon: 'question',
        input: 'password',
        inputLabel: 'Contraseña:',
        inputPlaceholder: 'Ingresa la contraseña',
        inputAttributes: {
            maxlength: 20,
            autocapitalize: 'off',
            autocorrect: 'off'
        },
        showCancelButton: true,
        confirmButtonText: 'Descargar',
        cancelButtonText: 'Cancelar',
        customClass: {
            confirmButton: 'btn btn-primary',
            cancelButton: 'btn btn-secondary',
            title: 'text-primary',
            input: 'form-control',
            container: 'swal2-question'
        },
        buttonsStyling: false,
        preConfirm: (password) => {
            return new Promise((resolve) => {
                setTimeout(() => {
                    if (password === '1234') {  // Reemplaza '1234' con la contraseña real
                        resolve();
                    } else {
                        Swal.showValidationMessage('Contraseña incorrecta');
                    }
                }, 1000);
            });
        }
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = url;  // Permite la descarga si la contraseña es correcta
        }
    });
}
