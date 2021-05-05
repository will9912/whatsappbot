from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

URL_IMAGEN = (
    "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    resp = MessagingResponse()
    try:
        num_media = int(request.values.get("NumMedia"))
    except (ValueError, TypeError):
        return "Invalid request: invalid or missing NumMedia parameter", 400
        
    msg = request.form.get("Body")

    if not num_media:
        resp.message("Hola William, escribiste esto: {}".format(msg))

    else:
        msg = resp.message("Se ha recibido el audio, aquí hay una imagen de ejemplo: ")
        msg.media(URL_IMAGEN)
    # Create reply
    
    resp.message("Hola, escribiste esto: {}".format(msg))
    resp.message("Esta es una prueba con Heroku")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)