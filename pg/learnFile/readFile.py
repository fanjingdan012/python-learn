def readFile():
    with open('./file.txt', 'r') as f:
        for line in f.readlines():
            print(line.strip())  # delete '\n'
        print(f.read())
if __name__=="__main__":
    readFile()