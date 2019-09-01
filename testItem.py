#!/user/bin/python3

class Item:

    def __init__(self):
        self.bread = 0
        self.eggs = 1
        pass



if (__name__ == "__main__"):
    item1 = Item()

    print("number of bread {}".format(item1.bread))

    print("number of eggs {}".format(item1.eggs))

    item1.bread += 1

    print("number of bread {}".format(item1.bread))

    item1.eggs += 4

    print("number of eggs {}".format(item1.eggs))


