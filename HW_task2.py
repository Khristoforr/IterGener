import hashlib

def main(path):
    with open(path,'r') as f:
        text = f.readlines()
        for string in text:
            yield hashlib.md5(string.encode()).hexdigest()

if __name__ == '__main__':
    for string in main('Task1'):
        print(string)