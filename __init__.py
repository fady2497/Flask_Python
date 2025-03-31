from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(valeur, 0, -1) , (1, valeur + 1):  
        for i in range(j):
            etoiles += ''
        etoiles += '<br>'
        return etoiles

if __name__ == "__main__":
    app.run(debug=True)
