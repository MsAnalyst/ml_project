# Importing required libs
from flask import Flask, flash, request, redirect, url_for, render_template

from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import os
from werkzeug.utils import secure_filename

# Instantiating flask app
app = Flask(__name__, static_folder='static')

UPLOAD_FOLDER = 'static/uploads/'
model = load_model('model3.h5')

app.secret_key = 'secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def predict_label(img_path):
    i = image.load_img(img_path, target_size=(224,224))
    i = image.img_to_array(i)
    i = i.reshape(1, 224, 224, 3)
    i = i/255

    p = model.predict(i)
    print(p)

    p = 'Normal' if p[0][0] > 0.1 else 'Stroke'
    return p

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('Tidak ada file nya')
        return redirect(request.url)

    file = request.files['file']

    # if file.filename == '':
    #     flash('Tidak ada gambar yang di upload')
    #     return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        prediction = predict_label(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('Gambar berhasil di upload dan di prediksi')

        print(filename)
        return render_template('result.html', filename=filename, prediction=prediction)

    else:
        flash('Kamu perlu upload file gambar dengan tipe .png .jpg')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


# Driver code
if __name__ == "__main__":
    app.run(debug=True)
