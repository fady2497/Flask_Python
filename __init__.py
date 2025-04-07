from flask import Flask

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice2(valeur):
    return ', '.join(map(str, 
        (lambda n: [0, 1] + [sum([0, 1][max(0, i-2):i]) for i in range(2, n)])(valeur)
    ))

if __name__ == '__main__':
    app.run(debug=True)
