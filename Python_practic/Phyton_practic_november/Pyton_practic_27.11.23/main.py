# flask --app main run --reload
from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

quotes = [
    "Цитата 1",
    "Цитата 2",
    "Цитата 3",
    "Цитата 4",
    "Цитата 5"
]


@app.get("/")
def hello():
    return {"hello": "world!"}, 201


@app.get("/current-day")
def show_current_day():
    day = datetime.now().strftime("%A")
    return f"Today is {day}"


@app.get('/quote')
def random_quote():
    random_quote = random.choice(quotes)
    return render_template('index.html', quote=random_quote)


if __name__ == '__main__':
    app.run()
