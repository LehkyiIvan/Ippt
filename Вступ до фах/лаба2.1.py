entr=""
list_a=[]
enter=str(int("Please choose A or B:"))
alphabet="АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгдеєжзиіїйклмнопрстуфхцчшщьюя"
if enter.upper()=="А"or enter.upper()=="А":
    a=input("Введіть текст>>>").split()
    for i in a:
        if(i not in list_a)and len(i)>2:
            list_a.append(i)
            list_a.sort()
            for x in range(0,len(list_a)):
                print(list_a[x])
elif enter.upper()=="В"or
enter.upper()=="В":
    a=input("Введіть текст>>>").split()
    for x in range(len(aphabet)):
        number=0
        for i in a:
            number=number+
i.count(alphabet[x])
if number>0:
    print(alphabet[x]+"-"+
str(number))
else:
    print(">>>ERROR<<<\nPlease enter A or B")
