from flask import Flask, jsonify, render_template
import generator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate")
def generate():
    return jsonify({"text": generator.generate_sentence()})

if __name__ == "__main__":
    app.run(debug = True) #turn off eventually


    