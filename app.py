from logging import debug
from flask import Flask, render_template, request
import config

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        q = request.form['q']
        books = config.searchBooks(q)
        return render_template('index.html', data=books)
    else:
        return render_template('index.html', data=[''])

if __name__ == '__main__':
    app.run(debug=True)