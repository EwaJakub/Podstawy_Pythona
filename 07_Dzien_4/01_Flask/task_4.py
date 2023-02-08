from flask import Flask

app = Flask(__name__)


@app.route("//licz/<int:number_1>/<int:number_2>", methods=["GET", "POST"])
def count(number_1, number_2):
    return f"Suma {number_1} i {number_2} wynosi {number_1 + number_2}!"


if __name__ == "__main__":
    app.run(debug=True)
