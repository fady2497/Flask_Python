from flask import Flask
from flask import render_template
from flask import json

app = Flask(name)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = '<pre>'
    for j in range(1, valeur + 1):
        espaces = ' ' * (valeur - j)
        etoiles += espaces + '' (1 * j - 1) + '\n'
    etoiles += '</pre>'
    return etoiles

if name == "main":
    app.run(debug=True)
