def count_valid_divisons(s, d, m):
    if m>len(s):
        return 0
    window_sum = sum(s[:m])
    count = 1 if window_sum == d else 0
    for i in range(m, len(s)):
        window_sum += s[i] - s[i - m]
        if window_sum ==d:
            count += 1
            return count
        s = [2, 2, 1, 3, 2]
        print(count_valid_divisons(s, d =4, m=2))