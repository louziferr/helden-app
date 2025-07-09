from flask import Flask, render_template, request, redirect

# App erstellen
app = Flask(__name__)

name = 'Naruto'
# TODO Daten aus db/helden.json laden
helden = ['Batman', 'Pikachu', 'Spongebob']

# Route definieren
@app.route('/')
def index():
    return render_template('index.html', name=name, helden=helden)

# zweite Route definieren
@app.route('/neu', methods=('GET', 'POST'))
def neu():
    if request.method == 'POST':
        neuer_name = request.form.get('neuer_name')
        helden.append(neuer_name)
        # TODO Neuen Namen in db/helden.json speichern
        return redirect('/')
    else:
        # Die Methode ist GET
        return render_template('neuer_name.html')

# App starten

print('App startet')

app.run(debug=True)