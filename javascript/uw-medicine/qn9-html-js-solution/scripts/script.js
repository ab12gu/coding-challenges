//*** */ main javascript file

//* project title
const message = 'Input Type Out'
document.querySelector('#header').innerHTML = message

//* Process button inputs
const recordButton = document.getElementById("recordButton");
let recordButtonVariable = "Start"; 
let recordHandlerText = ""
updateRecordButton(recordButtonVariable, recordHandlerText);

// function to update record button text
function updateRecordButton(recordButtonVariable, recordHandlerText){
    recordButtonText = `Press to ${recordButtonVariable} Recording`;
    document.querySelector('#recordButton').innerHTML = recordButtonText;
    document.querySelector('#record').innerHTML = recordHandlerText;
}

// Event handler for record button
let isRecording = false

recordButton.addEventListener("click", () => {
    if (isRecording == false) { // recording start
        recordHandlerText = "Recording Input Text";
        recordButtonVariable = `Stop`
        isRecording = true;
        events = []
    } else { // recording stop
        recordHandlerText = "Recording Stopped";
        document.querySelector('#record').innerHTML = recordHandlerText;
        recordButtonVariable = `Start`
        isRecording = false;
    }
    updateRecordButton(recordButtonVariable, recordHandlerText);

});

// Store keyboard inputs if record button is pressed
textarea.addEventListener("keydown", (event) => {
    if (isRecording) {
        events.push({
            type: "keydown", key: event.key
        })
    }
})

// Event handler for playback button
playbackButton.addEventListener("click", () => {
    document.getElementById("playbackText").innerHTML = "";
    i = 0;
    playback();
});

// playback the input text onto screen
function playback() {
    if (i < events.length) {
        document.getElementById("playbackText").innerHTML += events[i].key
        i++;
        setTimeout(playback, 100);
    }
}