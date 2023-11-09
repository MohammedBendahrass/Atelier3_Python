def Multiplication_Binaire(x, y):
    if x == "0" or y == "0":
        return "0"

    product = "0" * (len(x) + len(y))

    for i in range(len(y) - 1, -1, -1):
        if y[i] == "1":
            shafted_x = x + "0" * (len(y) - i - 1)
            product = ajouter_Strings_binaire(product, shafted_x)
    return product


def ajouter_Strings_binaire(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    carry = 0
    result = []

    for i in range(max_len - 1, -1, -1):
        x_bit = int(x[i])
        y_bit = int(y[i])

        xbit_sum = x_bit + y_bit + carry
        result.insert(0, str(xbit_sum % 2))
        carry = xbit_sum // 2

    if carry:
        result.insert(0, "1")
    return "".join(result)


x = "1100"
y = "1010"

product = Multiplication_Binaire(x, y)

print(product)
print(int(product, 2))
