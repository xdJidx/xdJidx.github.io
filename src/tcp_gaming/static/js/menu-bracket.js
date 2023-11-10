document.addEventListener('DOMContentLoaded', function () {
    // Perform an AJAX request to fetch the total number of tournaments
    fetch('http://localhost:8000/api/count-tournois/')
        .then(response => response.json())
        .then(data => {
            let totalTournaments = document.getElementById('nombre-tournois');
            totalTournaments.textContent = `Total tournaments: ${data.count}`;
            totalTournaments.classList.add('tournoi-number');
        })
        .catch(error => {
            console.error('Error fetching the total number of tournaments:', error);
        });

    // Perform an AJAX request to fetch the number of single tournaments
    fetch('http://127.0.0.1:8000/api/count-single/')
        .then(response => response.json())
        .then(data => {
            let singleTournaments = document.getElementById('result');
            singleTournaments.textContent = `Number of single tournaments: ${data.count}`;
            singleTournaments.classList.add('tournoi-number', 'single-tournoi');
        })
        .catch(error => {
            console.error('Error fetching the number of single tournaments:', error);
        });

    // Perform an AJAX request to fetch the number of double tournaments
    fetch('http://127.0.0.1:8000/api/count-double/')
    .then(response => response.json())
    .then(data => {
        let doubleTournaments = document.getElementById('double-result');
        doubleTournaments.textContent = `Number of double tournaments: ${data.count}`;
        doubleTournaments.classList.add('tournoi-number', 'double-tournoi');
    })
    .catch(error => {
        console.error('Error fetching the number of double tournaments:', error);
    });
});

