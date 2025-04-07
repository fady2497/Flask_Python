from flask import Flask

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    pyramide = ''
    for i in range(1, valeur + 1):
        ligne = ''
        ligne += '&nbsp;' * (valeur - i)
        for j in range(1, i + 1):
            ligne += str(j)
        for j in range(i - 1, 0, -1):
            ligne += str(j)
        pyramide += ligne + '<br>'
    
    html = f'''
    <html>
        <head>
            <title>Pyramide de chiffres</title>
        </head>
        <body style="font-family: monospace; text-align: center; margin-top: 50px;">
            <h2>Pyramide pour la valeur {valeur}</h2>
            <div style="line-height: 1.5;">
                {pyramide}
            </div>
        </body>
    </html>
    '''
    return html

if __name__ == "__main__":
    app.run(debug=True)
