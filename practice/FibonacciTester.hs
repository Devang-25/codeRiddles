-- fibPlus (fib i, fib (i + 1)) (fib j, fib (j + 1)) == (fib (i + j), fib (i + j + 1))
fibPlus (a, b) (c, d) = (bd - (b - a)*(d - c), a*c + bd) where bd = b*d

-- unFib (fib i, fib (i + 1)) n == (k, fib (i*k), fib (i*k + 1))
--   such that fib (i*k) <= n < fib ((i + 1)*k)
unFib (a, b) n
  | n < a = (0, 0, 1)
  | n < e = (2*k, c, d)
  | otherwise = (2*k + 1, e, f) where
    (k, c, d) = unFib (fibPlus (a, b) (a, b)) n
    (e, f) = fibPlus (a, b) (c, d)

isFib n = n == a where (k, a, b) = unFib (1, 1) n