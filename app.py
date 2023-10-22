from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from io import BytesIO
import os
from werkzeug.utils import secure_filename
import secrets

from time import sleep



app = Flask(__name__)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = secrets.token_hex(16)


@app.route('/')
def home():
    return render_template("Home.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # if request.method == 'POST':
    #     # check if the post request has the file part
    #     if 'file' not in request.files:
    #         flash('No file part')
    #         return redirect(request.url)
    #     file = request.files['file']
    #     # If the user does not select a file, the browser submits an
    #     # empty file without a filename.
    #     if file.filename == '':
    #         flash('No selected file')
    #         return redirect(request.url)
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         return redirect(url_for('download_file', name=filename))
    #     else:
    #         return redirect(request.url)
    if request.method == 'POST':
        files = request.files.getlist('files')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                buffered = BytesIO()
                file.save(buffered)
                image_buffer = buffered.getvalue()
                print(image_buffer)
                

                print("uploaded")
        return 'Files uploaded successfully!'
    


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)
        

            


# @app.route('/', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         try:

#             image = request.files['image']
#             image.save(os.path.join(UPLOADS_PATH, secure_filename(image.filename)))
#         except:
#             return render_template('index.html', results="No File Found")
#             return jsonify({'message': 'File uploaded successfully!'})
#     return jsonify({'message': 'No file selected.'})




# @app.route('/upload', methods=['POST'])
# def upload():
#     uploaded_file = requests.files['file']
#     if uploaded_file:
#         # Process the uploaded file here (e.g., save it to a specific directory)
#         # For example, to save it in the 'uploads' folder:
#         uploaded_file.save('uploads/' + uploaded_file.filename)
#         return jsonify({'message': 'File uploaded successfully!'})
#     return jsonify({'message': 'No file selected.'})


if __name__ == '__main__':
    app.run(debug=True)