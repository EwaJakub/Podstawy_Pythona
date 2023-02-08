from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def time_now():
    return datetime.now().strftime("%X")


if __name__ == "__main__":
    app.run(debug=True)