def safe_open(filename, mode):
    try:
        file = open(filename, mode)
        return file
    except:
        return None

print(safe_open('ch7.px', 'r'))
print(safe_open('1.py', 'r'))