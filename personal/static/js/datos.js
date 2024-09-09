document.addEventListener('DOMContentLoaded', () => {
    const flipContainers = document.querySelectorAll('.flip-container');

    flipContainers.forEach(container => {
        container.addEventListener('click', (event) => {
            const passwordCell = event.target.closest('.password-cell');
            const passwordCellda = event.target.closest('.password-cellda');

            if (passwordCell || passwordCellda) {
                const storedPassword = passwordCell ? passwordCell.dataset.password : passwordCellda.dataset.passwords;
                solicitarContraseñaMaestra(storedPassword);
            }

            container.classList.toggle('flipped');
        });
    });
});