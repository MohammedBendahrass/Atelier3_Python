def combination_sum(arr, x):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path.copy())
            return
        for i in range(start, len(arr)):
            if arr[i] > target:
                break
            path.append(arr[i])
            backtrack(i, target - arr[i], path)
            path.pop()

    result = []
    arr.sort()
    backtrack(0, x, [])
    return result


arr = [2, 3, 6, 7]
x = 7

result = combination_sum(arr, x)

if result:
    for combination in result:
        print(combination)
else:
    print("Vide")
