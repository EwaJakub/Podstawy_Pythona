from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template('task_7.html')
    elif request.method == "POST":
        name = request.form['name']
        return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
