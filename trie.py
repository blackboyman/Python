import random as rd
def generate_random_list(n,min, max):
    liste = []
    for i in range(n):
        liste.append(rd.randint(min, max))
    return liste

liste = generate_random_list(10,1,10)

print("Non trié :",liste)

def trier(liste):
    for index_non_trie in range(0, len(liste)):
        min = liste[index_non_trie]
        min_index = index_non_trie
        for index_std in range(index_non_trie+1, len(liste)):
            if liste[index_std] < min:
                min = liste[index_std]
                min_index =index_std
        liste[min_index] = liste[index_non_trie]
        liste[index_non_trie] = min
    return liste

print("Trié :",trier(liste))
