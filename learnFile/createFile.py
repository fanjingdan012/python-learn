def createFile():
    with open('./fileW.txt', 'w') as f:
        f.write('Hello, world!')


if __name__ == "__main__":
    createFile()