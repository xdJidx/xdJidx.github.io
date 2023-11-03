// Initiate the socket variable
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('roomForm').addEventListener('submit', function(event) {
        var roomName = document.getElementById('room_name').value.trim();
        var username = document.getElementById('username').value.trim();
        
        if (roomName === '' || username === '') {
            event.preventDefault();
            alert("Veuillez remplir les champs 'Room' et 'Username' avant de continuer.");
        }
    });
});