from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def methods_check():
    if request.method == "GET":
        return "Wysłałeś GET"
    elif request.method == "POST":
        return "Wysłałeś POST"


if __name__ == "__main__":
    app.run(debug=True)
