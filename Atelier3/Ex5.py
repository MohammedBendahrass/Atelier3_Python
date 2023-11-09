def calculate_min_product(arr1, arr2, size, k):
    difference = 0
    result = 0

    for val1, val2 in zip(arr1, arr2):
        product = val1 * val2
        result += product

        temp = (
            (val1 + 2 * k) * val2
            if product < 0
            else (val1 - 2 * k) * val2
            if product > 0
            else 0
        )

        difference = max(abs(product - temp), difference)

    return result - difference


array1 = [1, 2, -3]
array2 = [-2, 3, -5]
size = 3
k_value = 5
result = calculate_min_product(array1, array2, size, k_value)
print(result)
