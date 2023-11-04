document.addEventListener('DOMContentLoaded', function () {
    // Effectuer une requête AJAX pour récupérer le nombre total de tournois
    fetch('http://localhost:8000/api/count-tournois/')
        .then(response => response.json())
        .then(data => {
            let totalTournaments = document.getElementById('nombre-tournois');
            totalTournaments.textContent = `Total tournois: ${data.count}`;
            totalTournaments.classList.add('tournoi-number');
        })
        .catch(error => {
            console.error('Erreur lors de la récupération du nombre de tournois :', error);
        });

    // Effectuer une requête AJAX pour récupérer le nombre de tournois singles
    fetch('http://127.0.0.1:8000/api/count-single/')
        .then(response => response.json())
        .then(data => {
            let singleTournaments = document.getElementById('result');
            singleTournaments.textContent = `Nombre de tournois singles : ${data.count}`;
            singleTournaments.classList.add('tournoi-number', 'single-tournoi');
        })
        .catch(error => {
            console.error('Erreur lors de la récupération du nombre de tournois singles :', error);
        });
    });
