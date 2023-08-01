import math as mt
liste = [10,6,-5,5,30,-50,100]
liste.sort()
print(liste)

temperature = 0
n=0
p=0
for i in range(len(liste)-1):
    if liste[i] < 0:
        if liste[i+1]<0:
            n=liste[i+1]
        else:
            n=liste[i]
    else:
        p=liste[i]
        break

if mt.fabs(n) == mt.fabs(p):
    temperature = p
elif mt.fabs(n) < mt.fabs(p):
    temperature = n
else:
    temperature = p

print(n)
print()
print(p)
print("temperature :", temperature)