from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def formulaire():
    return '''
    <form action="/calcul" method="get">
        Entrez un nombre : <input type="number" name="n" min="1" required>
        <input type="submit" value="Calculer">
    </form>
    '''

@app.route('/calcul')
def calcul_somme():
    try:
        n = int(request.args.get('n'))
    except (ValueError, TypeError):
        return "Veuillez entrer un nombre valide."

    somme = 0

    for i in range(1, n + 1):
        # Si le nombre est divisible par 11, on passe au suivant
        if i % 11 == 0:
            continue

        # Si divisible par 5 ou 7, on l'ajoute à la somme
        if i % 5 == 0 or i % 7 == 0:
            somme += i

            # Si la somme dépasse 5000, on arrête immédiatement
            if somme > 5000:
                return f"La somme a dépassé 5000 et est : {somme}"

    # Si la boucle se termine normalement
    return f"La somme finale est : {somme}"

if __name__ == '__main__':
    app.run(debug=True)
