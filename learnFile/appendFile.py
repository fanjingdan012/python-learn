import random
def appendFile():
    with open('./fileW.txt', 'a') as f:
        for i in range(0, 10):
            f.write(str(random.randint(0, 9)))
            f.write('\n')
if __name__ == "__main__":
    appendFile()