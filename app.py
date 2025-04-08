from flask import Flask, request, Response
from plivo import plivoxml

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ Flask server is running!"

@app.route("/incoming-call", methods=["POST"])
def incoming_call():
    print("📞 Incoming call from Plivo:")
    print(request.form)

    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.SpeakElement("Hello, welcome to Tecnvirons. How may I assist you?")
    )

    return Response(response.to_string(), mimetype='text/xml')

if __name__ == "__main__":
    app.run(port=5000)