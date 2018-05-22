var socket = new WebSocket('ws://219.92.255.160:9000');

// Show a connected message when the WebSocket is opened.
socket.onopen = function(event) {
  console.log('WebSocket is connected.');
};

// The main logic to redirect current page to the URL we want upon receiving the data from websocket
// code after a pause of pause_before_start milliseconds
var pause_before_start = 100
setTimeout(function(){

    socket.onmessage = function(e) {
        console.log("Dwellers:" + e.data);
        if (e.data == ('[]') ) {
            //window.location.replace('nothing.html');
            console.log('nothing.html')
        }

        json = JSON.parse(e.data);

        for (var i = 0; i < json.length; i++){

        if (json[i]['person']) {
            console.log('person');
            if (json[i]['person'].location.includes(0) && json[i]['person'].location.includes(1) ) {
                console.log('person_in_the_middle.html')
                window.location.replace('person_in_the_middle.html');
            }
            if (json[i]['person'].location.includes(0) ){
                console.log('person_on_the_left.html');
                window.location.replace('person_on_the_left.html');
            }
            if (json[i]['person'].location.includes(1) ) {
                console.log('person_on_the_right.html');
                window.location.replace('person_on_the_right.html');
            }
        }        
        }
    }
    
    socket.onclose = function(e) {
        console.log("Connection closed (wasClean = " + e.wasClean + ", code = " + e.code + ", reason = '" + e.reason + "')");
        socket = null;
        window.location.replace('closed.html');
    }

}, pause_before_start);
