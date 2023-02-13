from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/losuj", methods=["GET"])
def los():
    numbers_list = ', '.join([str(randint(0, 100)) for _ in range(3)])
    return f"Wylosowane liczby to: {numbers_list}"


if __name__ == "__main__":
    app.run(debug=True)
