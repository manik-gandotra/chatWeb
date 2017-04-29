$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);
    
    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        var chat = $("#chat")
        var ele = $('<li class="left clearfix"></li>')
        var ele1 = $('<div class="chat-body "></div>')
        var ele2 = $('<div class="header" style="text-align: left;"></div>')
        var new_message = $('<p style="color: green" class="pull-right text-muted">New Message</p>')


        ele2.append(
            $("<strong  class='chat-participant' ><strong>").text(data.handle)
        )

        ele2.append(
            $('<small class="pull-right text-muted" style="margin-right: 10px;"><small>').text(data.timestamp)
        )
        ele2.append(new_message)
        ele2.append(
            $("<p class='message-text'></p>").text(data.message)
        )

        ele1.append(ele2)
        ele.append(ele1)
        chat.prepend(ele)
        $('#chat').load('chat/room.html', function() {

        });

    };

    $("#chatform").on("submit", function(event) {
        var message = {
            handle: $('#handle').val(),
            message: $('#message').val(),
        }
        chatsock.send(JSON.stringify(message));
        $("#message").val('').focus();
        return false;
    });
});