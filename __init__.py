from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def formulaire():
    return '''
    <form action="/calcul" method="get">
        Entrez un nombre : <input type="number" name="valeur" min="1" required>
        <input type="submit" value="Calculer">
    </form>
    '''

@app.route('/calcul')
def calcul_somme():
    try:
        n = int(request.args.get('valeur', 1))
    except ValueError:
        return "Veuillez entrer un nombre valide."

    somme = 0

    for i in range(1, n + 1):
        if i % 11 == 0:
            continue

        if i % 5 == 0 or i % 7 == 0:
            somme += i

            if somme > 5000:
                return f"La somme dépasse 5000 ! Somme actuelle : {somme}"

    return f"Somme finale : {somme}"

if __name__ == '__main__':
    app.run(debug=True)
