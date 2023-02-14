from flask import Flask, request, render_template

app = Flask(__name__)

def factiorial(n):
    s = 1
    for num in range(1, n + 1):
        s *= num
    return s


@app.route("/", methods=["GET", "POST"])
def natural_number():
    if request.method == "GET":
        return render_template('task_1.html')
    elif request.method == "POST":
        try:
            number = int(request.form['number'])
        except ValueError:
            return "Wartość niepoprawna"
        values = {
            'number': number,
            'exponentioantion_1': 2**number,
            'exponentioantion_2': number**number,
            'factorial': factiorial(number)
        }
        return render_template('task_1_POST.html', ctx=values)


if __name__ == "__main__":
    app.run(debug=True)
