# 간소화
def index(filename):
    try:
        with open(filename, 'r') as infile:
            infile.readlines()
    except:
        print("index('{}')\nFile '{}' not found".format(filename, filename))

index('rven.txt')