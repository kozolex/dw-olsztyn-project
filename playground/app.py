import os
from flask import Flask, render_template, request

__author__ = 'kozolex'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('/upload.html', methods=['POST'])

@app.route('/upload')
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        destination = '/'.join([target, filename])
        print(destination)
        file.save(destination)
    return render_template("complete.html")
    
if __name__ == "__main__":
    app.run(port=4555, debug=True)