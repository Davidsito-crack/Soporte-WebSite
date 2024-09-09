/*
// Función para filtrar los elementos de la tabla por sucursal
function filterBranches(branch) {
    const rows = document.querySelectorAll('.inventario tbody tr');
    const separators = document.querySelectorAll('.inventario tbody tr.separator');

    // Ocultar todos los elementos (items y separadores)
    rows.forEach(row => row.style.display = 'none');

    // Mostrar solo los elementos y separadores que coinciden con la sucursal seleccionada
    rows.forEach(row => {
        if (row.classList.contains('item')) {
            const rowBranch = row.querySelector('td:nth-child(6)').textContent.trim();
            if (branch === 'all' || rowBranch === branch) {
                row.style.display = '';
            }
        } else if (row.classList.contains('separator')) {
            const previousRow = row.previousElementSibling;
            if (previousRow && previousRow.style.display !== 'none') {
                row.style.display = '';
            }
        }
    });
}

// Función para mostrar/ocultar menú de sucursales
function showBranchesMenu() {
    const menu = document.getElementById('branches-menu');
    menu.classList.toggle('hidden');
}

// Función para mostrar/ocultar el menú de sucursales
function showBranchesMenu() {
    const menu = document.getElementById('branches-menu');
    menu.classList.toggle('hidden');
}

// Función para filtrar los elementos de la tabla por sucursal
function filterBranches(branch) {
    const rows = document.querySelectorAll('.inventario tbody tr.item');
    rows.forEach(row => {
        if (row.querySelector('td:nth-child(6)').textContent.trim() === branch || branch === 'all') {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
    updateSeparators();
}

// Función para actualizar los separadores
function updateSeparators() {
    const items = document.querySelectorAll('.inventario tbody tr.item');
    const separators = document.querySelectorAll('.inventario tbody tr.separator');

    // Ocultar todos los separadores inicialmente
    separators.forEach(separator => {
        separator.classList.add('hidden');
    });

    // Mostrar solo los separadores necesarios
    let previousItemType = null;
    items.forEach(item => {
        if (item.style.display !== 'none') {
            const itemType = item.classList[1];
            if (itemType !== previousItemType) {
                const separator = document.querySelector(`.inventario tbody tr.separator.${itemType}`);
                if (separator) {
                    separator.classList.remove('hidden');
                }
                previousItemType = itemType;
            }
        }
    });

    // Ajustar espacio si es necesario
    const visibleItems = Array.from(items).filter(item => item.style.display !== 'none');
    if (visibleItems.length > 0) {
        const firstVisibleItem = visibleItems[0];
        const previousElement = firstVisibleItem.previousElementSibling;
        if (previousElement && previousElement.classList.contains('separator')) {
            previousElement.classList.add('hidden');
        }
    }
}

// Función para actualizar los separadores entre elementos
function updateSeparators() {
    const items = document.querySelectorAll('.item');
    const separators = document.querySelectorAll('.separator');

    let previousItemType = null;

    items.forEach(item => {
        const itemType = item.classList[1]; // Obtener el tipo de elemento

        if (!item.classList.contains('hidden')) {
            // Mostrar separador si el tipo de elemento cambia
            if (itemType !== previousItemType) {
                const separator = document.querySelector('.separator'.$,{itemType});
                if (separator) {
                    separator.classList.remove('hidden');
                }
            }
            previousItemType = itemType;
        }
    });

    // Ocultar todos los separadores y mostrar solo los necesarios
    separators.forEach(separator => {
        const nextVisibleItem = separator.nextElementSibling;
        if (nextVisibleItem && nextVisibleItem.classList.contains('hidden')) {
            separator.classList.add('hidden');
        }
    });
}*/

// Función para filtrar elementos por tipo
function filterItems(type) {
    const rows = document.querySelectorAll('.inventario tbody tr');
    
    rows.forEach(row => {
        if (row.classList.contains('item')) {
            const itemType = row.classList[1]; // Obtener el tipo de elemento
            if (type === 'all' || itemType === type) {
                row.classList.remove('hidden'); // Mostrar fila que coincide
            } else {
                row.classList.add('hidden'); // Ocultar fila que no coincide
            }
        } else {
            row.classList.add('hidden'); // Ocultar cualquier otra fila (e.g., separadores)
        }
    });
    
    updateSeparators(); // Actualizar separadores para el filtrado por tipo
}

// Función para filtrar los elementos de la tabla por sucursal
function filterBranches(branch) {
    const rows = document.querySelectorAll('.inventario tbody tr');
    
    rows.forEach(row => {
        if (row.classList.contains('item')) {
            const rowBranch = row.querySelector('td:nth-child(6)').textContent.trim();
            if (branch === 'all' || rowBranch === branch) {
                row.classList.remove('hidden'); // Mostrar fila que coincide
            } else {
                row.classList.add('hidden'); // Ocultar fila que no coincide
            }
        } else {
            row.classList.add('hidden'); // Ocultar cualquier otra fila (e.g., separadores)
        }
    });
    
    updateSeparators(); // Actualizar separadores después del filtrado por sucursal
}

// Función para actualizar los separadores
function updateSeparators() {
    const items = document.querySelectorAll('.inventario tbody tr.item:not(.hidden)');
    const separators = document.querySelectorAll('.inventario tbody tr.separator');
    
    // Ocultar todos los separadores inicialmente
    separators.forEach(separator => {
        separator.classList.add('hidden');
    });
    
    // Mostrar separadores entre los elementos visibles
    let previousItemType = null;
    items.forEach(item => {
        const itemType = item.classList[1];
        if (itemType !== previousItemType) {
            const separator = document.querySelector(`.inventario tbody tr.separator.${itemType}`);
            if (separator) {
                separator.classList.remove('hidden');
            }
            previousItemType = itemType;
        }
    });
}

// Función para mostrar/ocultar menú de sucursales
function showBranchesMenu() {
    const menu = document.getElementById('branches-menu');
    menu.classList.toggle('hidden');
}
