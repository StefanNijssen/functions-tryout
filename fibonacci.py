def optellen(num1):
    x = 1
    y = 1
    for i in range(1,num1+1):
        if x == 1:
            x += 1
            y = x
        else:
            x = y + x

        

aantal = int(input("Hoeveelste cijfer wilt u weten?"))

optellen(aantal)