// This script is used to redirect the user to the tournament bracket page
document.addEventListener('DOMContentLoaded', function() {
const buttons = document.querySelectorAll('.join-btn');
buttons.forEach(button => {
button.addEventListener('click', function() {
    const tournamentId = this.getAttribute('data-id');
    const url = `http://127.0.0.1:8000/model-bracket/?tournament_id=${tournamentId}`;
    window.location.assign(url);
});
});
});