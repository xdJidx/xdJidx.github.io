document.addEventListener('DOMContentLoaded', function () {
    // Effectuer une requête AJAX pour récupérer le nombre total de tournois
    fetch('http://localhost:8000/api/count-tournois/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('nombre-tournois').textContent = `totals tournois: ${data.count}`;
        })
        .catch(error => {
            console.error('Erreur lors de la récupération du nombre de tournois :', error);
        });

    // Effectuer une requête AJAX pour récupérer le nombre de tournois commençant par "single"
    fetch('http://127.0.0.1:8000/api/count-single/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').textContent = `Nombre de single tournois : ${data.count}`;
        })
        .catch(error => {
            console.error('Erreur lors de la récupération du nombre de tournois :', error);
        });

    // Effectuer une requête AJAX pour récupérer le nombre de tournois commençant par "double"
    fetch('http://127.0.0.1:8000/api/count-double/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('double-result').textContent = `Nombre de double tournois : ${data.count}`;
        })
        .catch(error => {
            console.error('Erreur lors de la récupération du nombre de tournois :', error);
        });
});