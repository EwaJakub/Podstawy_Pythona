from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def zip_code():
    if request.method == "GET":
        return render_template('task_2.html')
    elif request.method == "POST":
        code = request.form['code']
        try:
            if isinstance(int(code[0:2]), int) \
                    and isinstance(int(code[-3:]), int) \
                    and code[2] == '-' \
                    and len(code) == 6:
                return "Kod poprawny"
            else:
                return "Kod niepoprawny"
        except ValueError:
            return "Kod niepoprawny"


if __name__ == "__main__":
    app.run(debug=True)
