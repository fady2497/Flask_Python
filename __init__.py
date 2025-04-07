
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
          <title>Pyramide de nombres</title>
      </head>
      <body style="font-family: monospace; background-color: #1e1e2e; color: white; padding: 20px;">
          <h3>Exemple de pyramide générée pour une valeur = {valeur} :</h3>
          <div style="background-color: #2b2b3c; padding: 10px; border-radius: 10px; display: inline-block; text-align: left;">
              {pyramide}
          </div>
      </body>
  </html>
  '''
  return html

if __name__ == "__main__":
  app.run(debug=True)
