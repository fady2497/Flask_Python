from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = '<pre>'
    for j in range(1, valeur + 1):  
        etoiles += ' ' * (valeur - j) + '*' * (1 * j - 1) + '\n'  
    etoiles += '</pre>'
    return etoiles

if __name__ == "__main__":
    app.run(debug=True)
