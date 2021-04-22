def collision(r, x, y, r1, x1, y1):
    if (x-x1)**2+(y-y1)**2 <= (r+r1)**2:
        return True
    else:
        return False


print(collision(3, 0, 0, 3, 0, 5))
print(collision(1.4, 0, 0, 1.4, 2, 2))
