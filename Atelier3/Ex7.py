def generate_subsets(arr):
    def backtrack(start, path):
        result.append(path.copy())
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result


arr = [1, 2, 3]

subsets = generate_subsets(arr)

for subset in subsets:
    print(subset)
