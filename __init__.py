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

    html = f'''
    <html>
        <head>
            <title>Pyramide de nombres</title>
        </head>
        <body style="font-family: monospace; margin: 20px;">
            <h2>Exemple de pyramide générée pour une valeur = {valeur} :</h2>
            <div style="background-color: #1e1e2e; color: white; padding: 10px; border-radius: 8px;">
                {pyramide}
            </div>
        </body>
    </html>
    '''
    return html

if __name__ == "__main__":
    app.run(debug=True)

