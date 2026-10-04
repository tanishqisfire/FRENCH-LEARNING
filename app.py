from flask import Flask, jsonify, render_template, request, send_file
import generator
import tts

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate")
def generate():
    global latest_value
    latest_value = generator.generate_sentence()
    return jsonify({"text": latest_value})

@app.route("/speak")
def speak():
    text = request.args.get("text", "  ")
    if not text:
        return jsonify({"error": "no text given"}), 400
    audio_path = tts.text_to_speech(text)
    return send_file(audio_path, mimetype = "audio/wav")

if __name__ == "__main__":
    app.run(debug = True) #turn off eventually


    