def add2D(fir, sec):
    for i in range(len(fir)):
        for k in range(len(fir)):
            fir[i][k]+=sec[i][k]
    return fir

t=[[4,7,2,5], [5,1,9,2],[8,3,6,6]]
s=[[0,1,2,0], [0,1,1,1], [0,1,0,0]]

add2D(t,s)
for row in t:
    print(row)
