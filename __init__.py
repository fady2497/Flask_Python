from flask import Flask

app = Flask(__name__)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    liste_nombres = valeurs.split('/')
    liste_nombres = [int(n) for n in liste_nombres]
    resultat = 0
    for n in liste_nombres:
        resultat = resultat + n
    return str(resultat)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
