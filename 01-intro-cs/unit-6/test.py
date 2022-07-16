def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n - 1)