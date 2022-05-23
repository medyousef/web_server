from flask import Flask
import RPi.GPIO as GPIO
import time
LED_LIST=[14,23,24]
Button_PIN =18
GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_PIN, GPIO.IN)
app=Flask(__name__)
for led in LED_LIST:
    GPIO.setup(led,GPIO.OUT)
    GPIO.output(led, GPIO.LOW)


#routes
@app.route("/")
def index():
    return "hello from flask"

@app.route("/push-button")
def push_button():
    if GPIO.input(Button_PIN)== GPIO.HIGH:
        return "Button is pressed"
    return "not pressed"
@app.route("/led/<int:led_pin>/state/<int:led_state>")
def trigger_led(led_pin,led_state):
    if led_pin not in LED_LIST:
        return "led no in the list"
    if led_state==1:
        state=GPIO.HIGH
        GPIO.output(led_pin, state)
        return
    elif led_state==0:
        state=GPIO.LOW
        GPIO.output(led_pin, state)
        return 
    else:
        return "wrong state"

    return
app.run(host="0.0.0.0", port=5000)
