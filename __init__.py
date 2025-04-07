from flask import Flask

app = Flask(__name__)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    liste_nombres = valeurs.split('/')
    liste_nombres = [int(n) for n in liste_nombres]

    plus_grand = None

    for nombre in liste_nombres:
        if plus_grand is None or nombre > plus_grand:
            plus_grand = nombre

    return f"Le nombre maximum est : {plus_grand}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
