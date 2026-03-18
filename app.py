from flask import Flask, render_template, request, jsonify
from utils.chatbot import get_ai_response
from utils.ocr_reader import read_prescription
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.json["message"]
    reply = get_ai_response(user_msg)
    return jsonify({"response": reply})


@app.route("/upload", methods=["GET","POST"])
def upload():

    text = ""

    if request.method == "POST":
        file = request.files["image"]
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        text = read_prescription(path)

    return render_template("upload.html", text=text)


if __name__ == "__main__":
    app.run(debug=True)
