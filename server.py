from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def decorator(function):
    def text_wrapper(*args, **kwargs):
        return f"<h1 style='text-align: center; color: yellow; background-color: black; width: 300px'>You guessed " \
               f"{args[0]}:</h1> {function(args[0])}"

    return text_wrapper


@decorator
def too_low(number):
    return "<h2 style='color: purple'>Too high, try again!</h2>" \
           "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"


@decorator
def too_high(number):
    return "<h2 style='color: red'>Too low, try again!</h2>" \
           "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"


@decorator
def correct_number(number):
    return "<h2 style='color: green'>You found me!</h2>" \
           "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


@app.route("/")
@make_emphasis
def greet():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def compare(guess):
    if guess > random_number:
        return too_low(guess)

    elif guess < random_number:
        return too_high(guess)

    else:
        return correct_number(guess)


if __name__ == "__main__":
    app.run(debug=True)
