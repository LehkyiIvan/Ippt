# а, б, в, г, ґ, д, е,
# є, ж, з, и, і, ї, й,
# к, л, м, н, о, п, р,
# с, т, у, ф, х, ц, ч,
# ш, щ, ь, ю, я

word = input("Word: ")
res = ""
for letter in word:
    if ord(letter) == ord('я'):
        res+='а'
    else:
        res += chr(ord(letter)+1)
print(res)

#chr -конвертує цифру в букву
# ord - конвертує букву в цифру 
