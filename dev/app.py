# from flask import Flask, request, jsonify
# from nudenet import NudeClassifier
# import json


# app = Flask(__name__)
# classifier = NudeClassifier()


# @app.route('/classify')
# def classify():
#     try:
      
#         # Call the classify_image function
#         result = classifier.classify('C:\\Users\\Admin\\Desktop\\Flask Learn\\dev\\pic2.jpeg')

#         return jsonify(result)

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, request, jsonify,render_template,flash,redirect
# from nudenet import NudeClassifier
# import io

# app = Flask(__name__)
# classifier = NudeClassifier()

# def process_image(file):
#     # Convert the uploaded file to an image
#     image_bytes = file.read()
#     return image_bytes

# @app.route('/')
# def home():
#     return render_template('index.html')

# ALLOWED_EXTENSIONS=set(['png','jpg','jpeg','gif'])

# def allowed_file(filename):
#     return "."in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
# @app.route('/classify', methods=['POST'])
# def classify():
#     # try:
#     #     # Check if the request contains a file
#     #     if 'file' not in request.files:
#     #         return jsonify({'error': 'No file part'}), 400

#     #     file = request.files['file']

#     #     # Check if the file has a name
#     #     if file.filename == '':
#     #         return jsonify({'error': 'No selected file'}), 400

#     #     # Process the image
#     #     image_bytes = process_image(file)

#     #     # Call the classify_image function
#     #     result = classifier.classify(image_bytes)
#     #     print(result)
#     #     return jsonify(result)

#     # except Exception as e:
#     #     return jsonify({'error': str(e)}), 500

#     if 'file' not in request.files:
#         flash("No file part")
#         return redirect(request.url)
    
#     file=request.files['file']

#     if(file.filename ==''):
#         flash('No image Sleected for uploading')
#         return redirect(request.url)
    


# if __name__ == '__main__':
#     app.run(debug=True)

#app.py
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
 
if __name__ == "__main__":
    app.run()