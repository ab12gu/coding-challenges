const textarea = document.getElementById("myTextarea");
const playbackContainer = document.getElementById("playbackContainer");
const recordButton = document.getElementById("recordButton");
const playbackButton = document.getElementById("playbackButton");

let events = [];
let isRecording = false;

recordButton.addEventListener("click", () => {
  isRecording = true;
  events = [];
  console.log("Recording started");
});

playbackButton.addEventListener("click", () => {
  playback();
});

textarea.addEventListener("keydown", (event) => {
  if (isRecording) {
    events.push({ type: "keydown", key: event.key });
  }
});

textarea.addEventListener("input", (event) => {
  if (isRecording) {
    events.push({ type: "input", value: event.target.value });
  }
});

function playback() {
  playbackContainer.innerHTML = ""; // Clear previous playback
  events.forEach((event) => {
    if (event.type === "keydown") {
      textarea.value += event.key;
    } else if (event.type === "input") {
      textarea.value = event.value;
    }

    // Simulate typing delay
    setTimeout(() => {
      // Trigger input event for visual feedback (optional)
      textarea.dispatchEvent(new Event("input"));
    }, 50); // Adjust delay as needed
  });
}
