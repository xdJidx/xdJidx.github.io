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

// Fonction pour créer un participant
function createParticipant() {
    const createParticipantBtn = document.getElementById('createParticipantBtn');
    createParticipantBtn.style.display = 'none'; // Masquer le bouton
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
            
            // Procéder à la création du participant
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
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Impossible de créer le participant');
            }
            return response.json();
        })
        .then(data => {
            console.log('Participant créé :', data);

            // Définition de currentPlayerId dans le localStorage après la création du participant
            localStorage.setItem('currentPlayerId', data.id);

            // Actualiser la page après la création du participant
            location.reload();
        })
        .catch(error => {
            console.error('Erreur :', error);
            createParticipantBtn.style.display = 'block'; // Réafficher le bouton en cas d'erreur
        });
}
// Ajout de l'écouteur d'événements pour le bouton de création de participant
document.addEventListener('DOMContentLoaded', function() {
    const createParticipantBtn = document.getElementById('createParticipantBtn');
    if (createParticipantBtn) {
        createParticipantBtn.addEventListener('click', createParticipant);
    }
});



// Ajout de l'écouteur d'événements pour l'exécution de getCounts lorsque la page est chargée
document.addEventListener('DOMContentLoaded', getCounts);

// Fonction pour afficher la liste des participants
function displayParticipants(tournamentId) {
    let storedParticipants = localStorage.getItem(`participants_${tournamentId}`);
    
    if (storedParticipants) {
        storedParticipants = JSON.parse(storedParticipants);
        displayParticipantsList(storedParticipants);
    } else {
        fetch(`http://127.0.0.1:8000/api/participants/?tournoi=${tournamentId}`)
            .then(response => response.json())
            .then(participants => {
                participants.sort(() => 0.5 - Math.random());
                localStorage.setItem(`participants_${tournamentId}`, JSON.stringify(participants));
                displayParticipantsList(participants);
            })
            .catch(error => console.error('Error:', error));
    }
}
// Fonction pour afficher la liste des participants dans le DOM
function displayParticipantsList(participants) {
    participants.forEach((participant, index) => {
        let playerDiv = document.getElementById(`player${index + 1}`);
        if (playerDiv) {
            playerDiv.textContent = participant.nom;
        }
    });
}
// Fonction pour obtenir le nombre de participants
function getCounts() {
    if (!tournamentId) {
        console.error('Aucun ID de tournoi spécifié dans l\'URL');
        return;
    }

    fetch(`http://127.0.0.1:8000/api/count-participants-per-tournoi/?tournoi=${tournamentId}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            let resultsDiv = document.getElementById('results');
            const tournoiNom = Object.keys(data)[0];
            const participantCount = data[tournoiNom];
            resultsDiv.innerHTML = `${tournoiNom}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ${participantCount} /8 Participants<br>`;
            
            if (participantCount >= 8) {
                displayParticipants(tournamentId);
            }
        })
        .catch(error => console.error('Error:', error));
}



// Fonction pour obtenir l'ID du joueur actuel à partir du localStorage
function getCurrentPlayerId() {
    return localStorage.getItem('currentPlayerId');
}

// Fonction pour récupérer l'index de l'utilisateur actuel parmi les participants
function getCurrentUserIndex(tournamentId) {
    const storedParticipants = JSON.parse(localStorage.getItem(`participants_${tournamentId}`));
    const currentUser = getCurrentPlayerId(); // Récupérez l'ID de l'utilisateur actuel

    if (storedParticipants && currentUser) {
        for (let i = 0; i < storedParticipants.length; i++) {
            if (storedParticipants[i].id === currentUser) {
                return i; // Retourne l'index de l'utilisateur actuel
            }
        }
    }
    return -1; // Retourne -1 si l'utilisateur actuel n'est pas trouvé
}

// Utilisation de l'ID du tournoi récupéré de l'URL
const urlParam = new URLSearchParams(window.location.search);
const tournamentsId = urlParam.get('tournament_id');
console.log('ID du tournoi récupéré de l\'URL:', tournamentsId);

// Utilisation de l'ID du tournoi pour obtenir l'index de l'utilisateur actuel
const userIndex = getCurrentUserIndex(tournamentsId);

if (userIndex !== -1) {
    console.log(`L'utilisateur actuel se trouve à l'index ${userIndex}`);
} else {
    console.log("L'utilisateur actuel n'a pas été trouvé parmi les participants lol.");
}


// Fonction pour afficher l'index du current user
function showUserIndex() {
    const urlParams = new URLSearchParams(window.location.search);
    const tournamentId = urlParams.get('tournament_id');

    // Utilisation de l'ID du tournoi pour obtenir l'index de l'utilisateur actuel
    const userIndex = getCurrentUserIndex(tournamentId);

    if (userIndex !== -1) {
        alert(`L'index de l'utilisateur actuel est : ${userIndex}`);
    } else {
        alert("L'utilisateur actuel n'a pas été trouvé parmi les participants.");
    }
}

// Ajout d'un écouteur d'événements pour le bouton
const showUserIndexBtn = document.getElementById('showUserIndexBtn');
if (showUserIndexBtn) {
    showUserIndexBtn.addEventListener('click', showUserIndex);
}




function updateScore() {
    var scoreElement = document.getElementById('score8');
    scoreElement.textContent = 'V';
    
    // Change la couleur du texte
    scoreElement.style.color = '#FF8E53';
  }

function scoredefeat() {
    var scoreElement = document.getElementById('score8');
    scoreElement.textContent = 'D';
    scoreElement.style.color = 'black';
}

