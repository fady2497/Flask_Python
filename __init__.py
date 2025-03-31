from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    # Premier motif
    etoiles_1 = ''
    for j in range(valeur):
        for i in range(valeur - j):  
            etoiles_1 += '*'
        etoiles_1 += '<br>'
    
    # Deuxième motif
    etoiles_2 = ''
    for j in range(valeur):
        for i in range(j + 1):  
            etoiles_2 += '*'
        etoiles_2 += '<br>'
    
    # Retourner les deux motifs dans un format HTML
    return f"<pre>{etoiles_1}</pre><br><pre>{etoiles_2}</pre>"

if __name__ == "__main__":
    app.run(debug=True)

