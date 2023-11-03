// Fonction pour obtenir la valeur d'un cookie par son nom
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Est-ce que ce cookie commence par le nom recherché ?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Récupération de l'ID du tournoi à partir de l'URL
const urlParams = new URLSearchParams(window.location.search);
const tournamentId = urlParams.get('tournament_id');
console.log('ID du tournoi récupéré de l\'URL:', tournamentId);

// Fonction pour vérifier si le participant existe déjà
function participantExists(username, tournamentId) {
    return fetch(`http://127.0.0.1:8000/api/participants/?nom=${username}&tournoi=${tournamentId}`)
        .then(response => response.json())
        .then(data => data.length > 0); // Supposons que l'API retourne un tableau de participants
}

// Fonction pour créer un participant
function createParticipant() {
    const csrftoken = getCookie('csrftoken');
    fetch('/api/get-user/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Impossible de récupérer les données de l’utilisateur');
            }
            return response.json();
        })
        .then(data => {
            console.log('Données utilisateur récupérées:', data);
            // Vérifier d'abord si le participant existe
            return participantExists(data.username, tournamentId).then(exists => {
                if (exists) {
                    throw new Error('Le participant existe déjà pour cet utilisateur et ce tournoi');
                }
                // Si le participant n'existe pas, procéder à la création
                return fetch('http://127.0.0.1:8000/api/participants/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken,
                    },
                    body: JSON.stringify({
                        nom: data.username,
                        tournoi: tournamentId,
                    })
                });
            });
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Impossible de créer le participant');
            }
            return response.json();
        })
        .then(data => {
            console.log('Participant créé :', data);
        })
        .catch(error => {
            console.error('Erreur :', error);
        });
}

// Ajout de l'écouteur d'événements au bouton
document.getElementById('create-participant-btn').addEventListener('click', createParticipant);
