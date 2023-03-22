import flask
from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key="LICjeevanbima"


@app.route('/')
def home_func():
    return render_template('layout.html')

@app.route('/login', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        session["username"] = request.form["username"]
        return redirect(url_for('note_func'))
    return render_template("login.html")

notes = []
@app.route('/note', methods=["GET", "POST"])
def note_func():
    if request.method=="POST":
        note = request.form.get("note")
        notes.append(note)
        return render_template("note.html", notes=notes)
    return render_template("note.html")

@app.route('/out', methods=['GET','POST'])
def logout_func():
    if request.method=='POST':
        session.pop('username', None)
        notes.clear()
        return redirect(url_for('home_func'))
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)