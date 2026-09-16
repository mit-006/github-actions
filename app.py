from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
<<<<<<< HEAD
    return render_templatee('index.html') --fix
=======
    return render_templatee('index.html')
>>>>>>> a655e3b5db808c3126aef7c1b7bf03050af180a1
