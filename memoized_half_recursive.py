class MemoizedHalfRecursive:
    def __init__(self, n: int):
        self.f = [-1] * (n + 1)  # memo array
        self.f[1] = self.f[2] = 1  # base cases
        self.value = self.rec_half_fib(n)

    def rec_half_fib(self, n: int) -> int:
        if self.f[n] == -1:
            half_n = n >> 1
            if n & 1:
                self.f[n] = self.rec_half_fib(half_n + 1) ** 2 + self.rec_half_fib(half_n) ** 2
            else:
                self.f[n] = self.rec_half_fib(half_n) * (2 * self.rec_half_fib(half_n + 1) - self.rec_half_fib(half_n))
        return self.f[n]


def memoized_half_recursive(n: int) -> int:
    p = MemoizedHalfRecursive(n)
    return p.value
