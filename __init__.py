from flask import Flask
from flask import render_template

app = Flask(_name_)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = '<pre>'
    for j in range(1, valeur + 1):  
        etoiles += ' ' * (valeur - j) + '*' * (2 * j - 1) + '\n'  
    etoiles += '</pre>'
    return etoiles

if _name_ == "_main_":
    app.run(debug=True)
