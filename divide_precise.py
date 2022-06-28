def divide(n1,n2,p):
    res = ""
    while True:
        count = 0
        while n1 < n2:
            n1 *= 10
            if len(res) == 0:
                count += 1
                res += "0."
            else:
                count += 1
                if count > 1:
                    res += str(0)
        d = float(n1/n2)
        i = str(d).index(".")
        num_floor = int(str(d)[:i])
        if count == 0:
            res += str(num_floor)+"."
        else:
            res += str(num_floor)
        n1 = n1 - num_floor * n2

        if len(res)-1 >= p or n1 == 0:
            break
    if len(res) < p:
        z = p - len(res)
        res += "0"*z

    print(res)

n1 = float(input("Enter value of numerator "))
n2 = float(input("Enter value of denominator "))
p = int(input("Enter precision of division. Please this should be an integer "))

divide(n1,n2,p)