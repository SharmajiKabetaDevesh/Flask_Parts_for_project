# from flask import Flask, render_template, request, jsonify
# from nudenet import NudeDetector

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/share-image', methods=['POST'])
# def share_image():
#     # Get the uploaded image file
#     image = request.files['image']


# # initialize classifier (downloads the checkpoint file automatically the first time)

# # Classify single image
#     # Process the image using your nudity detection model
#     # Replace the following line with your actual model integration
#     # For demonstration purposes, let's assume a function `detect_nudity` is available
#     nude_detector = NudeDetector()
#     result=nude_detector.detect(image) # Returns list of detections

#     # Return the result as JSON
#     return jsonify({'result': result})

# # Function to simulate nudity detection (replace with your actual implementation)
# def detect_nudity(image):
#     # Replace this with your actual nudity detection logic
#     # For now, let's assume it always returns 'safe'
#     return 'safe'


# @app.route('/send-message', methods=['POST'])
# def send_message():
#     message = request.form['message']

#     # Process the text message using your offensive language detection model
#     # Replace the following line with your actual model integration
#     # For demonstration purposes, let's assume a function `detect_offensive_language` is available
#     result = detect_offensive_language(message)

#     # Return the result as JSON
#     return jsonify({'result': result})

# # Function to simulate offensive language detection (replace with your actual implementation)
# def detect_offensive_language(message):
#     # Replace this with your actual offensive language detection logic
#     # For now, let's assume it always returns 'safe'
#     return 'safe'

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from nudenet import NudeDetector

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/share-image', methods=['POST'])
def share_image():
    image = request.files['image']
    nude_detector = NudeDetector()
    result = nude_detector.detect(image)

    # Emit the result to all connected clients
    socketio.emit('image_result', {'result': result})
    return jsonify({'result': result})

@app.route('/send-message', methods=['POST'])
def send_message():
    message = request.form['message']
    result = detect_offensive_language(message)

    # Emit the result to all connected clients
    socketio.emit('text_result', {'result': result})
    return jsonify({'result': result})

def detect_offensive_language(message):
    # Replace this with your actual offensive language detection logic
    # For now, let's assume it always returns 'safe'
    return 'safe'

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('server_message', {'data': 'Connected'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True)
