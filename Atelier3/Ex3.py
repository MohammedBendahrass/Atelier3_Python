def Min_palindrome(s):
    n = len(s)

    is_palindrome = [[False] * n for _ in range(n)]

    for i in range(n):
        is_palindrome[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                is_palindrome[i][j] = s[i] == s[j]
            else:
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]

    cuts = [float("inf")] * n

    for j in range(n):
        if is_palindrome[0][j]:
            cuts[j] = 0

        else:
            for i in range(j, 0, -1):
                if is_palindrome[i][j]:
                    cuts[j] = min(cuts[j], cuts[i - 1] + 1)

    return cuts[n - 1]


string_Exe = "ababbbabbababa"
result = Min_palindrome(string_Exe)
print(f"Le nombre minimum de coupes pour une partition palindrome : {result}")
