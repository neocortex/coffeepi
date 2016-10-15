from time import sleep

import RPi.GPIO as GPIO
from flask import Flask, render_template
from flask_apscheduler import APScheduler

from config import Config

app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

RELAIS = 17 

GPIO.setmode(GPIO.BCM) # use GPIO numbers instead of board 
GPIO.setup(RELAIS, GPIO.OUT)

data = {'is_on': False, 'status': 'OFF', 'todo': 'on'}

def update_status(action):
    global data
    if action == 'on':
	data['is_on'] = True
        data['status'] = 'ON'
        data['todo'] = 'off'
    if action == 'off':
	data['is_on'] = False 
        data['status'] = 'OFF'
        data['todo'] = 'on'
	

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/coffee/on')
def turn_on(): 
    print('Turning on...')
    GPIO.output(RELAIS, GPIO.HIGH)
    update_status('on')
    return render_template('index.html', data=data)

@app.route('/coffee/off')
def turn_off():
    wait_time = 3
    GPIO.output(RELAIS, GPIO.HIGH)
    sleep(wait_time)
    GPIO.output(RELAIS, GPIO.LOW)
    sleep(wait_time)
    GPIO.output(RELAIS, GPIO.HIGH)
    sleep(wait_time)
    GPIO.output(RELAIS, GPIO.LOW)
    update_status('off')
    return render_template('index.html', data=data)

@app.route('/coffee/start')
def start_coffee():
    turn_on()
    sleep(30)
    turn_off()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, use_reloader=False)
