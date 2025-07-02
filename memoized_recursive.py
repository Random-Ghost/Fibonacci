class MemoizedRecursive:
    def __init__(self, n: int):
        self.f = [-1] * (n + 1)
        self.f[1] = self.f[2] = 1
        self.value = self.rec_fib(n)

    def rec_fib(self, n: int) -> int:
        if self.f[n] == -1:
            self.f[n] = self.rec_fib(n - 1) + self.rec_fib(n - 2)
        return self.f[n]


def memoized_recursive(n: int) -> int:
    p = MemoizedRecursive(n)
    return p.value
