from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def formulaire():
    return '''
    <h2>Exercice 2 : Suite de calculs (Un = Un-1 + Un-2)</h2>
    <form action="/suite" method="get">
        Entrez un nombre : <input type="number" name="valeur" min="2" required>
        <input type="submit" value="Générer la suite">
    </form>
    '''

@app.route('/suite')
def calcul_suite():
    try:
        n = int(request.args.get('valeur', 2))
    except (ValueError, TypeError):
        return "❌ Veuillez entrer un nombre valide.", 400

    if n < 2:
        return "❌ Le nombre doit être au moins 2.", 400

    suite = [0, 1]
    for _ in range(2, n):
        suite.append(suite[-1] + suite[-2])

    # Mise en forme propre de l'affichage
    suite_str = ', '.join(map(str, suite))
    return f'''
    <h2>Résultat de l'exercice 2</h2>
    <p>Pour n = {n}, la suite est :</p>
    <p><strong>{suite_str}</strong></p>
    <a href="/">🔙 Retour</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
