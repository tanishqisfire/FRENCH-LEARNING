const generatebtn = document.getElementById("generateBtn");
const box = document.getElementById("textBox");


generatebtn.addEventListener("click", async () => {
    box.textContent = "Generating...";
    try {
        const res = await fetch("/generate");
        const data = await res.json();

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