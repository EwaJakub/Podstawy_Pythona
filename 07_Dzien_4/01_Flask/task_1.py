from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Witaj użytkowniku!"

@app.route("/hello/<string:name>")
def hello_name(name):
    return f"Witaj użytkowniku {name}!"


if __name__ == "__main__":
    app.run(debug=True)
