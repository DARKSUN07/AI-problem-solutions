def inp():
    a = int(input("Enter capacity of 1st jug: "))
    b = int(input("Enter capacity of 2nd jug: "))
    n = int(input("How much water do you want in 1st jug: "))

    if n >= a or a == b or a < b:
        print("Invalid input!\n\n")
        inp()

    else:
        Istate = [a,0]
        check(Istate,a,b,n)

def check(Istate,a,b,n):

    if Istate[0] <= 0:
        Istate[0] = a
    
    print(Istate)

    if Istate[0] == n:
        return 0

    if Istate[0] <= a and Istate[0] > 0:
        temp = Istate[0]
        Istate[0] = Istate[0] - (b - Istate[1])
        if temp + Istate[1] < b:
            Istate[1] = temp + Istate[1]
            Istate[0] = 0
            print(Istate)
        else:
            Istate[1] = b
            print(Istate)
            Istate[1] = 0
        check(Istate,a,b,n)

inp()