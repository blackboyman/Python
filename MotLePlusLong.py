def get_min_and_max_words(sentense):
    max_word = max(sentense.split(" "), key=len)
    min_word = min(sentense.split(" "), key=len)
    return min_word,max_word

text = "COULIBALY Karamoko née le 13/02 à Katiola"

word = get_min_and_max_words(text)
min_word = word[0]
max_word = word[1]
print("Le mot le plus court est :", min_word)
print("Le mot le plus long est :", max_word)

def get_min_and_max_words_by_aplha(sentense):
    word = sentense.split(" ")
    word.sort()
    max_word = max(word, key=len)
    min_word = min(word, key=len)
    return min_word,max_word

text = "karamoky karamokz Aoulibaly Coulibaly née le 13/02 à Katiola"

min_word, max_word = get_min_and_max_words_by_aplha(text)

print("Le mot le plus court est :", min_word)
print("Le mot le plus long est :", max_word)