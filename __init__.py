from flask import Flask

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    pyramide = ''
    for i in range(1, valeur + 1):
        ligne = ''
        # Partie croissante
        for j in range(1, i + 1):
            ligne += str(j)
        # Partie décroissante
        for j in range(i - 1, 0, -1):
            ligne += str(j)
        pyramide += ligne + '<br>'
    return pyramide
