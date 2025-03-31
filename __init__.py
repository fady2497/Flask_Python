from flask import Flask
from flask import render_template
from flask import json
app = Flask(name)


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(1, valeur + 1):
        etoiles += '' j + '<br>'
    return etoiles

if name == "main":
    app.run(debug=True)
