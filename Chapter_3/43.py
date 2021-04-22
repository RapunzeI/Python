def hit(Cx, Cy, r, Px, Py):
    if r**2 >= (Px-Cx)**2+(Py-Cy)**2:
        return True
    else:
        return False


print(hit(0, 0, 3, 3, 0))
print(hit(0, 0, 3, 4, 0))
