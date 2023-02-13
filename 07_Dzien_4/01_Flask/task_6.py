from flask import Flask
from random import sample

app = Flask(__name__)


@app.route("/lotek", methods=["GET"])
def lotek():
    lista = [str(x) for x in range(1, 50)]
    numbers_list = ', '.join(sample(lista, 6))
    return f"Wylosowane liczby to: {numbers_list}"


if __name__ == "__main__":
    app.run(debug=True)
