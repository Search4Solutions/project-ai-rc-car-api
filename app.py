from flask import Flask, request, render_template
import RPi.GPIO as GPIO
app = Flask(__name__)

motorDriveForwardPin = 4 #7
motorDriveReversePin = 17 #11
motorSteerLeftPin = 27 #13
motorSteerRightPin = 22 #15
motorDrivePWM = 5 #29
motorSteerPWM = 6 #31

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

pwm_drive = GPIO.PWM(motorDrivePWM, 10000)
pwm_steer = GPIO.PWM(motorSteerPWM, 10000)

#If no endpoint is called, then show the usage page.
@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

#Direction endpoint
@app.route('/direction', methods=['POST'])
def set_direction():
    #First check if APIKey is correct.
    entered_apikey = request.args.get('apikey')
    f = open('secrets', 'r')
    secret = f.readline()
    if secret != entered_apikey:
        return 'Invalid API key.', 401
    
    #Check if there's a parameter in the form.
    parameter = request.form.get('direction')
    if not parameter:
        return 'No parameter given in form.', 400
    
    #Check which direction is provided, return 'bad request' if invalid direction is given.
    direction = request.form['direction']
    if direction == 'forward':
        pwm_drive.start(100)
        GPIO.output(motorDriveForwardPin, GPIO.HIGH)
        GPIO.output(motorDriveReversePin, GPIO.LOW)
        return 'Moving forward.'
    elif direction == 'reverse':
        pwm_drive.start(100)
        GPIO.output(motorDriveForwardPin, GPIO.LOW)
        GPIO.output(motorDriveReversePin, GPIO.HIGH)
        return 'Moving backwards.'
    elif direction == 'left':
        if GPIO.input(motorSteerLeftPin):
            GPIO.output(motorSteerLeftPin, GPIO.LOW)
            pwm_steer.stop()
            return 'Stopped turning left.'
        else:
            pwm_steer.start(100)
            GPIO.output(motorSteerRightPin, GPIO.LOW)
            GPIO.output(motorSteerLeftPin, GPIO.HIGH)
            return 'Turning left.'
    elif direction == 'right':
        if GPIO.input(motorSteerRightPin):
            GPIO.output(motorSteerRightPin, GPIO.LOW)
            pwm_steer.stop()
            return 'Stopped turning right.'
        else:
            pwm_steer.start(100)
            GPIO.output(motorSteerLeftPin, GPIO.LOW)
            GPIO.output(motorSteerRightPin, GPIO.HIGH)
            return 'Turning right.'
    else:
        return 'Invalid direction parameter.', 400

#Speed endpoint
@app.route('/speed', methods=['POST'])
def set_speed():
    #First check if APIKey is correct.
    entered_apikey = request.args.get('apikey')
    f = open('secrets', 'r')
    secret = f.readline()
    if secret != entered_apikey:
        return 'Invalid API key.', 401
	
	#Check if there's a parameter in the form.
    parameter = request.form.get('speed')
    if not parameter:
        return 'No parameter given in form.', 400
    
    #Check which speed is provided, return 'bad request' if invalid speed is given.
    speed = request.form['speed']
    if speed == 'slow':
        #Not yet implemented.
        return 'Speed set to slow.'
    elif speed == 'medium':
        #Not yet implemented.
        return 'Speed set to medium.'
    elif speed == 'fast':
        #Not yet implemented.
        return 'Speed set to fast.'
    elif speed == 'stop':
        pwm_drive.stop()
        GPIO.output(motorDriveForwardPin, GPIO.LOW)
        GPIO.output(motorDriveReversePin, GPIO.LOW)
        return 'Car has stopped.'
    else:
        return 'Invalid speed parameter.', 400