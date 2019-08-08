from flask import Flask, request, render_template
app = Flask(__name__)

#If no endpoint is called, then show the usage page.
@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

#Direction endpoint
@app.route('/direction', methods=['POST'])
def set_direction():
    #First check if there's a parameter in the form.
    parameter = request.form.get('direction')
    if not parameter:
        return 'No parameter given in form.', 400
    
    #Check which direction is provided, return 'bad request' if invalid direction is given.
    direction = request.form['direction']
    if direction == 'forward':
        return 'Moving forward.'
    elif direction == 'reverse':
        return 'Moving backwards.'
    elif direction == 'left':
        return 'Turning left.'
    elif direction == 'right':
        return 'Turning right.'
    else:
        return 'Invalid direction parameter.', 400

@app.route('/speed', methods=['POST'])
def set_speed():
    #First check if there's a parameter in the form.
    parameter = request.form.get('speed')
    if not parameter:
        return 'No parameter given in form.'
    
    #Check which speed is provided, return 'bad request' if invalid speed is given.
    speed = request.form['speed']
    if speed == 'slow':
        return 'Speed set to slow.'
    elif speed == 'medium':
        return 'Speed set to medium.'
    elif speed == 'fast':
        return 'Speed set to fast.'
    elif speed == 'stop':
        return 'Car has stopped.'
    else:
        return 'Invalid speed parameter.', 400