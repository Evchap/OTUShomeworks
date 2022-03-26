from flask import (
    Flask,
    render_template,
    url_for,
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about/")
def about():
    return render_template('about.html')

with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))


if __name__ == "__main__":
    app.run(debug=True)