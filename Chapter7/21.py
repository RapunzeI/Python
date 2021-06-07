def safe_input():
    try:
        x = input()
        return x
    except KeyboardInterrupt:
        return 'x'
print(safe_input())