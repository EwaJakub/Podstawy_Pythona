from flask import Flask, request, render_template
from exam import movies


app = Flask(__name__)


@app.route("/movies/", methods=["GET", "POST"])
def movies_view():
    if request.method == "GET":
        return render_template('answer6.html')
    elif request.method == "POST":
        try:
            title = request.form['title']
            if title in movies['favourite']:
                return 'favourite'
            elif title in movies["hated"]:
                return 'hated'
            else:
                return 'no such movie!'
        except TypeError:
            return 'no such movie!'

if __name__ == "__main__":
    app.run(debug=True)
