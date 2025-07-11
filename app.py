from flask import Flask, render_template, request, redirect
import json

# App erstellen
app = Flask(__name__)

name = 'Naruto'

# Daten aus db/helden.json laden
with open('db/helden.json', encoding='utf-8') as f:
    helden = json.load(f)

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
        # Neuen Namen in db/helden.json speichern
        with open('db/helden.json', 'w', encoding='utf-8') as f:
            json.dump(helden, f)
        return redirect('/')
    else:
        # Die Methode ist GET
        return render_template('neuer_name.html')
    
    # Route definieren
@app.route('/held')
def held():
    name = request.args.get('name')
    # TODO Website für einen einzelnen Helden implementieren
    return name

# App starten
app.run(debug=True)