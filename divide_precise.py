def divide(n1, n2, p):
    if n2 == 0:
        print("Error: Division by zero is not allowed.")
        return

    # Performing integer division to get the integer part
    integer_part = int(n1 // n2)
    remainder = n1 - integer_part * n2
    res = str(integer_part) + "."

    # Loop to get the decimal part with the required precision
    for _ in range(p):
        remainder *= 10
        digit = int(remainder // n2)
        res += str(digit)
        remainder -= digit * n2

        if remainder == 0:
            break

    # Adding trailing zeros if necessary to match the required precision
    if len(res.split(".")[1]) < p:
        res += "0" * (p - len(res.split(".")[1]))

    print(res)


n1 = float(input("Enter value of numerator: "))
n2 = float(input("Enter value of denominator: "))
p = int(input("Enter precision of division. Please, this should be an integer: "))

divide(n1, n2, p)
