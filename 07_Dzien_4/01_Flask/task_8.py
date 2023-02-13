from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template('task_8.html')
    elif request.method == "POST":
        action = request.form['action']
        number_1 = int(request.form['number_1'])
        number_2 = int(request.form['number_2'])
        if action == 'summary':
            result= number_1 + number_2
        elif action == 'subtraction':
            result = number_1 - number_2
        elif action == 'multiplication':
            result = number_1 * number_2
        elif action == 'division':
            try:
                result = number_1 / number_2
            except ZeroDivisionError:
                result = "Nie dzielimy przez 0 !"
        return render_template('task_8_POST.html', ctx=result)


if __name__ == "__main__":
    app.run(debug=True)