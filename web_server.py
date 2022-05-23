from flask import Flask
import RPi.GPIO as GPIO
Button_PIN =18
GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_PIN, GPIO.IN)
app=Flask(__name__)

#routes
@app.route("/")
def index():
    return "hello from flask"

@app.route("/push-button")
def push_button():
    if GPIO.input(Button_PIN)== GPIO.HIGH:
        return "Button is pressed"
    return "not pressed"
app.run(host="0.0.0.0", port=5000)
