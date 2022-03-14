from flask import Flask, redirect, render_template, request, redirect, session, flash, url_for
app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('index.html',title= 'Atenas Intranet') 


if __name__ == "__main__":
    app.run(debug=True)
