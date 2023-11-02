document.addEventListener("DOMContentLoaded", function () {
    $(document).ready(function(){
    var display = $("#display");
    setInterval(function(){
        $.ajax({
            type: 'GET',
            url : "/getMessages/{{room}}/",
            success: function(response){
                console.log(response);
                var isAtBottom = display.scrollTop() + display.innerHeight() >= display[0].scrollHeight;
                $("#display").empty();
                for (var key in response.messages)
                {
                    var rawDate = new Date(response.messages[key].date);
                    var formattedDate = rawDate.toLocaleString('fr-FR', {day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute:'2-digit'});
                    var temp="<div class='darker'><b>"+response.messages[key].user+"</b><p>"+response.messages[key].value+"</p><span>"+formattedDate+"</span></div>";
                    $("#display").append(temp);
                }
                // Scroll to the bottom of the chat window if the user is already at the bottom
                if (isAtBottom) {
                    $("#display").scrollTop($("#display")[0].scrollHeight);
                }
            },
            error: function(response){
                alert('An error occured')
            }
        });
    },500);
    });
});