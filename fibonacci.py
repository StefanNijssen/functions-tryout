def optellen(num1):
    x = 0
    y = 0
    for i in range(1,num1-2):
        if x == 0:
            x += 1
        else:
            x = y + x
            y = x + y
            
    if num1 // 2 == 0:
        print(y)
    else:
        print(x)

    

        

aantal = int(input("Hoeveelste cijfer wilt u weten?"))

optellen(aantal)