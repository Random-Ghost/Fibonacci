def half_recursive(n: int) -> int:
    if (n == 1) or (n == 2):  # base cases
        return 1
    half_n = n >> 1  # right bit shift, divide n by 2
    if n & 1:  # check if n is odd
        return half_recursive(half_n + 1) ** 2 + half_recursive(half_n) ** 2  # F_2n+1 = F_n+1 ^ 2 + F_n ^ 2
    else:  # F_2n = F_n(2F_n-1 + F_n)
        return half_recursive(half_n) * (2 * half_recursive(half_n - 1) + half_recursive(half_n))
