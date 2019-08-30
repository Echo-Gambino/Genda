from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('welcomePage.html')


@app.route("/user")
def main():
    return render_template('mainPage.html')

if __name__ == "__main__":
    app.run()
    pass




