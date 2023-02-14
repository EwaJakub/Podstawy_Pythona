from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def personal_form():
    if request.method == "GET":
        return render_template('task_11.html')
    elif request.method == "POST":
        name = request.form['name']
        surname = request.form['surname']
        personal_data = {
            'name': name,
            'surname': surname
        }
        return render_template('task_11_POST.html', ctx=personal_data)


if __name__ == "__main__":
    app.run(debug=True)
