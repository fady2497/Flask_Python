from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = '<pre>'
    for j in range(1, valeur + 1):  
        espaces = ' ' * (valeur - j)  
        etoiles += espaces + '*' * (2 * j - 1) + '\n'
    etoiles += '</pre>'
    return etoiles

if __name__ == "__main__":
    app.run(debug=True)
