
with open('./c.py', 'r') as f:
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉
    print(f.read())