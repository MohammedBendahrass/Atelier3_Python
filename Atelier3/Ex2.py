def Racine_Carree(n):
    if n < 0:
        raise ValueError("le nombre qui est entrer est negatif")

    if n == 0 or n == 1:
        return n

    left, right = 0, n

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == n:
            return mid

        elif mid * mid <= n:
            left = mid + 1
        else:
            right = mid - 1

    return right


num = int(input(f"Entrer un nombre : "))
Racine = Racine_Carree(num)

print(f"Le racine carree de nombre {num} est approximativement : {Racine}")
