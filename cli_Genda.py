from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('welcomePage.html')


@app.route("/user")
def main():

    items = [
            'hello',
            'there',
            'man'
            ]

    return render_template('mainPage.html', **locals())

if __name__ == "__main__":
    app.run()
    pass




