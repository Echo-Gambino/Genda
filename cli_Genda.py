from flask import Flask, flash, redirect, render_template, request, session, abort


class Item:

    def __init__(self):
        self.title = ""
        self.data = ""
        pass


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('welcomePage.html')


@app.route("/user")
def main():

    feed = list()

    for i in range(0, 15):
        itm = Item()
        itm.title = "Title #{}".format(i)
        # itm.data = "something something something something something something something something something something something something something something something"
        data = ""
        for x in range(0, 35):
            data += "something {} ".format(x)
        itm.data = data

        feed.append(itm)
    
    print("number of items in feed: {}".format(len(feed)))

    items = [
            'hello',
            'there',
            'man'
            ]

    for i in range(0, 15):
        items.append('item' + str(i))

    return render_template('mainPage.html', **locals())


if __name__ == "__main__":
    app.run()
    pass




