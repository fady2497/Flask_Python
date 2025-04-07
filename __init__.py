from flask import Flask

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice2(valeur):
    suite = [0, 1]  
    for _ in range(2, valeur):
        suite += [suite[-1] + suite[-2]]  
    return ', '.join(map(str, suite)) 

if __name__ == '__main__':
    app.run(debug=True)
