from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/', methods=['GET', 'POST' ])
def index():
    user_note = request.form.get("note")
    if (user_note != ""):
        notes.append(user_note)

    elem = None
    if elem in notes:
        notes.remove(elem)
    return render_template("home.html", notesss=notes)


if __name__ == '__main__':
    app.run(debug=True)