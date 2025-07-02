def inefficient_recursive(n: int) -> int:  # the slowest of the bunch
    if (n == 1) or (n == 2):
        return 1
    return inefficient_recursive(n - 1) + inefficient_recursive(n - 2)
