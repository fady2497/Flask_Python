from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def formulaire():
    return '''
    <form action="/suite" method="get">
        Entrez un nombre : <input type="number" name="valeur" min="2" required>
        <input type="submit" value="Générer">
    </form>
    '''

@app.route('/suite')
def calcul_suite():
    try:
        n = int(request.args.get('valeur', 2))
    except ValueError:
        return "Veuillez entrer un nombre valide", 400
    
    if n < 2:
        return "Le nombre doit être au moins 2", 400
    
    suite = [0, 1]
    for i in range(2, n):
        suite.append(suite[-1] + suite[-2])
    
    return f"Suite pour n={n} : {', '.join(map(str, suite))}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
