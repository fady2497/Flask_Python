from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def calcul_somme_securise(n):
    somme = 0
    nombres_ajoutes = []
    
    for nombre in range(1, n + 1):
        if nombre % 11 == 0:
            continue
            
        if nombre % 5 == 0 or nombre % 7 == 0:
            if somme + nombre > 5000:
                break
            somme += nombre
            nombres_ajoutes.append(str(nombre))
    
    return (
        f"Résultat pour n={n}<br><br>"
        f"Nombres ajoutés: {', '.join(nombres_ajoutes)}<br><br>"
        f"Somme finale: {somme} (garantie ≤ 5000)"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
