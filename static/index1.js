const btn = document.getElementById("generateBtn");
const box = document.getElementById("textBox");


btn.addEventListener("click", async () => {
    box.textContent = "Generating...";
    try {
        const res = await fetch("/generate");
        const data = await res.json();

        box.textContent = data.text;
    
    } catch(err) {
        box.textContent = "Error: " + err;
    }
})