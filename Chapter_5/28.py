def geometric(sequence):
    for i in range(len(sequence)-2):
        if sequence[i+1]**2!=sequence[i]*sequence[i+2]:
            return False

    return True

print(geometric([2,4,8,16,32,64,128,256]))
print(geometric([2,4,6,8]))