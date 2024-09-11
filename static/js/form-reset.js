// Asegurar que el código se ejecute cuando el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const alertSuccess = document.querySelector('.alert-success');

    if (alertSuccess && form) {
        // Si se muestra un mensaje de éxito, reseteamos el formulario
        form.reset();
    }
});
