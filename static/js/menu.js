// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    // Seleccionar el botón de menú y el menú
    const menuToggle = document.getElementById('menu-toggle');
    const menu = document.getElementById('menu');

    // Añadir un listener de eventos al botón de menú
    menuToggle.addEventListener('click', function() {
        // Alternar la clase 'active' en el menú
        menu.classList.toggle('active');
    });
});
