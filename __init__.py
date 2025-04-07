from flask import Flask

app = Flask(__name__)

@app.route('/suite/<int:n>')
def suite(n):
    a, b = 0, 1
    suite = []

    for _ in range(n):
        suite.append(str(a))
        a, b = b, a + b

    resultat = ', '.join(suite)
    return f"<pre>{resultat}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
