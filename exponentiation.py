def exponentiation_helper(n: int) -> list:
    f = [1, 1, 0]
    if n == 1:
        return f
    x_half_n = exponentiation_helper(n >> 1)  # [a, b, c] since it is always symmetrical
    x = [x_half_n[0] ** 2 + x_half_n[1] ** 2,  # just the formula for the square
         (x_half_n[0] + x_half_n[2]) * x_half_n[1],  # of a symmetric matrix
         x_half_n[1] ** 2 + x_half_n[2] ** 2]
    if n & 1:
        return [x[0] + x[1], x[0], x[1]]  # x(x^n)^2
    else:
        return x  # (x^n)^2


def exponentiation(n: int) -> int:
    return exponentiation_helper(n - 1)[0]
