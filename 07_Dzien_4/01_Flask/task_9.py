from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)

choosen_number = randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def guess_number():
    if request.method == "GET":
        return render_template('task_9.html')
    elif request.method == "POST":
        number = int(request.form['number'])
        if number == choosen_number:
            result = "Gratulacje, udało Ci się!"
        elif number > choosen_number:
            result = "za dużo!"
        elif number < choosen_number:
            result = "za mało!"
        return render_template('task_9.html', ctx=result)


if __name__ == "__main__":
    app.run(debug=True)
