sentence = input("Enter here> ")
dictionary = {}

def sort_func(l):
    return ord(l.upper())

for letter in sentence:
    if(letter not in dictionary):
        dictionary[letter] = 1
    else:
        dictionary[letter] += 1

arr = [l for l in sentence]

arr.sort(key=sort_func)
print(str.format("Sorted by letters: {0}",arr));
for l,c in dictionary.items():
    print(str.format("{0} - {1}",l,c))
