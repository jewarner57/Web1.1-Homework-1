from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def homepage():
    # display a greeting to the user
    return "Are you there, world? It's me, Ducky!"


@app.route("/penguins")
def penguins():
    # display a phrase about penguins
    return "Penguins are cute!"


@app.route("/animal/<users_animal>")
def favorite_animal(users_animal):
    # display a message using the users favorite animal
    return f"Wow, {users_animal} is my favorite animal, too!"


@app.route("/dessert/<users_dessert>")
def favorite_dessert(users_dessert):
    # display a message using the user's favorite dessert
    return f"How did you know I liked {users_dessert}?"


@app.route("/madlibs/<adjective>/<verb>")
def madlibs(adjective, verb):
    # display a funny phrase using user input
    return f"Remote learning is {adjective}. I hope I learn how to {verb}"


@app.route("/multiply/<number1>/<number2>")
def multiply(number1, number2):
    # display the product of 2 numbers

    result = str(int(number1) * int(number2))

    if number1.isdigit() and number2.isdigit():
        return number1 + " times " + number2 + " is " + result + "."
    return "Invalid inputs. Please try again by entering 2 numbers!"


# Stretch
@app.route("/sayntimes/<word>/<n>")
def sayntimes(word, n):
    # display the word n times
    if not n.isdigit():
        return "Invalid input. Please try again by entering a word and a number!"

    response = (word + " ") * int(n)
    return response


@app.route("/reverse/<word>")
def reverse(word):
    # display the reversed version of the word
    reversedWord = ""
    for letter in word:
        reversedWord = letter + reversedWord

    return reversedWord


@app.route("/strangecaps/<word>")
def strangecaps(word):
    # display the word with alternating caps
    strangeWord = ""
    for letter in word:
        if len(strangeWord) % 2 == 1:
            strangeWord = strangeWord + letter.upper()
        else:
            strangeWord = strangeWord + letter.lower()

    return strangeWord


@app.route("/dicegame")
def dicegame():
    # display the result of the dice game
    roll = random.randint(1, 6)

    if roll == 6:
        return "You rolled a 6. You won!"

    return "You rolled a " + str(roll) + ". You lost!"


if __name__ == "__main__":
    app.run(debug=True)
