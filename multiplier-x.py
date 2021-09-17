tafel = int(input("Van welk getal wilt u de tafel zien?\n"))
def multiplier(tafel: int):
    x = 0
    for i in range(1,12):      
        print(str(tafel*x))
        x += 1
multiplier(tafel)
