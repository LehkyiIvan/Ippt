word = input("Введіть слово: ")
res = "";
for i in range(len(word)):
    res += word[len(word) - i -1 ]
print(res)



#range(len(word)) масив з букв
#len(word) овжина слова
#i- лічильник
