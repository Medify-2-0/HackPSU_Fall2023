from flask import Flask, render_template

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}


@app.route('/')
def home():
    return render_template("Home.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)