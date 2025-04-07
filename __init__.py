from flask import Flask
app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''

    for j in range(1, valeur + 1):
        etoiles += '&nbsp;' * (valeur - j)
        for i in range(1, j + 1):
            etoiles += str(i)
        for i in range(j - 1, 0, -1):
            etoiles += str(i)
        etoiles += '<br>'

    a, b = 0, 1
    suite = [a, b]
    for _ in range(2, valeur):
        suivant = suite[-1] + suite[-2]
        suite.append(suivant)

    etoiles += '<br><strong>Exercice 2 : Suite de calculs</strong><br>'
    etoiles += ', '.join(map(str, suite))

    return etoiles

if __name__ == "__main__":
    app.run(debug=True)
