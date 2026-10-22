from flask import Flask, jsonify, render_template, request, send_file
import generator
import tts
from pipeline import check_pronounciation



app = Flask(__name__)

latest_value = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate")
def generate():
    global latest_value
    try:
     latest_value = generator.generate_sentence()
    except Exception as e:
     print("Generator error:", e)
     return jsonify({"error": "Could not generate a sentence, try again in a moment."}), 500
    return jsonify({"text": latest_value})

@app.route("/speak")
def speak():
    text = request.args.get("text", "  ")
    if not text:
        return jsonify({"error": "no text given"}), 400
    audio_path = tts.text_to_speech(text)
    return send_file(audio_path, mimetype = "audio/wav")

@app.route("/check", methods=["POST"])
def check():
    audio_file = request.files.get("audio")

    if audio_file is None:
        return jsonify({"error": "no audio given"}), 400
    if latest_value is None: 
        return jsonify({"error": "generate a sentence first"}), 400

    audio_file.save("recording.wav")
    results = check_pronounciation(latest_value, "recording.wav")
    return jsonify({"results": results})




if __name__ == "__main__":
    app.run(debug = True) #turn off eventually


    