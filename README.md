Here we have the simple recursive formula for the Fibonacci numbers.
```math
F_{n + 2} = F_{n + 1} + F_n
```
From this it is easy to get recursive algorithms.

But it is faster to use the following formulas,
```math
\begin{align*}
  F_{2n + 1} &= F_{n + 1}^2 + F_n^2 \\
  F_{2n} &= (2F_{n + 1} - F_n)F_n
\end{align*}
```
as we will be able to calculate this in $` O(log(n)) `$ time compared to $` O(n) `$ in the memoized recursive algorithm.

It is also possible to get it in $` O(log(n)) `$ time by using matrices and it uses less space.
