a = float(input("a= "))
b = float(input("b= "))
s = input("Оберіть операцію */+-")
if s == '+':
    print(a+b)
elif s== '/':
    if b==0:
        print("Не можна ділити на 0")
    else:
        print(a/b) 
elif s == '-':
    print(a-b)
elif s == '*':
    print(a*b)
    

