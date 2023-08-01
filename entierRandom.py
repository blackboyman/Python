import random as rd
def generate_random_list(n,min, max):
    liste = []
    for i in range(n):
        liste.append(rd.randint(min, max))
    return liste
print(generate_random_list(10,1,10))