def sliding_window(n: int) -> int:
    f = [1, 0]
    if n == 1:
        return f[0]
    for i in range(n - 1):  # since we only need (n-1) multiplications according to the formula
        f = [f[0] + f[1], f[0]]  # this is just the matrix multiplication
    return f[0]
