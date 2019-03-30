def find_digit (num, nth):
    if nth < 0:
        print (-1)
    elif nth > len(str(num)):
        print (0)
    else:
        print (str(num)[-nth])
find_digit(num=int(input("Enter numbers: ")),nth=int(input("Enter num: ")))
