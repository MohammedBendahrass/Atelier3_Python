def Can_Partition(arr):
    total_sum = sum(arr)

    if total_sum < 0:
        return (
            False,
            "Le Tableau ne peut pas etre divisé en ensembles de sommes égales.",
            None,
            None,
        )

    target_sum = total_sum // 2

    memo = {}

    def is_partition_Possible(current_index, current_sum):
        if current_sum == target_sum:
            return True

        if current_index < 0 or current_sum > target_sum:
            return False

        if (current_index, current_sum) in memo:
            return memo[(current_index, current_sum)]

        current_inclure = is_partition_Possible(
            current_index - 1, current_sum + arr[current_index]
        )
        current_exclude = is_partition_Possible(current_index - 1, current_sum)

        memo[(current_index, current_sum)] = current_inclure or current_exclude

        return memo[(current_index, current_sum)]

    result = is_partition_Possible(len(arr) - 1, 0)

    if result:
        partition1 = []
        partition2 = []
        current_index = len(arr) - 1
        current_sum = 0

        while current_index >= 0:
            if current_sum + arr[current_index] <= target_sum and is_partition_Possible(
                current_index - 1, current_sum + arr[current_index]
            ):
                partition1.append(arr[current_index])

                current_sum += arr[current_index]
            else:
                partition2.append(arr[current_index])

            current_index -= 1
        return (
            result,
            "Le tableau peut etre divisé en deux ensembles de sommes égales.",
            partition1,
            partition2,
        )

    else:
        return (
            result,
            "Le tableau ne peut pas etre divisé en ensembles de sommes égales",
            None,
            None,
        )


arr1 = [1, 5, 11, 5]
arr2 = [1, 5, 3]

result1, message1, partition1, partition2 = Can_Partition(arr1)
result2, message2, _, _ = Can_Partition(arr2)

print(f"Sortie Pour Arr1 : {message1}")
if result1:
    print(f"Ensemble1 : {partition1}")
    print(f"Ensemble2 : {partition2}")

print(f"Sortie Pour Arr2 : {message2}")
