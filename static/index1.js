const generatebtn = document.getElementById("generateBtn");
const box = document.getElementById("textBox");
const recordBtn = document.getElementById("recordBtn");
const resultBox = document.getElementById("resultBox");

generatebtn.addEventListener("click", async () => {
    box.textContent = "Generating...";
    resultBox.textContent = "";
    try {
        const res = await fetch("/generate");
        const data = await res.json();
        
        if (data.error) {
            box.textContent = data.error;
            return;
        }
        box.textContent = data.text;
    
    } catch(err) {
        box.textContent = "Error: " + err;
    }
})


const speakbtn = document.getElementById("speakBtn");

speakbtn.addEventListener("click", async () => {
    const text = box.textContent;
    const audio = new Audio("/speak?text=" + encodeURIComponent(text));

    audio.play()
});

let mediaRecorder = null;
let chunks = [];

recordBtn.addEventListener("click", async () => {
    if (mediaRecorder && mediaRecorder.state === "recording") 
        {
        mediaRecorder.stop();
        recordBtn.textContent = "Record";
        return;
    }

    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true});
        mediaRecorder = new MediaRecorder(stream);
        chunks = [];

        mediaRecorder.ondataavailable = (event) => {
            chunks.push(event.data)
        };

        mediaRecorder.onstop = async () => {
            stream.getTracks().forEach((track) => track.stop());
            const blob = new Blob(chunks, { type: mediaRecorder.mimeType });
            await sendRecording(blob);
        };

        mediaRecorder.start()
        recordBtn.textContent = "Stop";
        resultBox.textContent = "Recording...";}
    catch (err) {
      resultBox.textContent = "Microphone error: " + err;

      }
    
});

async function sendRecording(blob) {
    resultBox.textContent = "Checking...";
    const formData = new FormData();
    formData.append("audio", blob, "recording.webm");

    try {
        const res = await fetch("/check", { method: "POST", body: formData });
        const data = await res.json();


        if (data.error) {
            resultBox.textContent = data.error;
            return;
        }

        resultBox.textContent = "";
        const words = box.textContent.trim().split(/\s+/);
        if (words.length !== data.results.length) {
            resultBox.textContent = "Could not match words to results";
            return;
        }
       

        data.results.forEach((item, index) => {
            const span = document.createElement("span");
            span.textContent = words[index] + " ";
            span.className = item.ok? "word-ok" : "word-bad";
            resultBox.appendChild(span);
        });
    } catch(err) {
        resultBox.textContent = "Error: " + err;
    }
}
