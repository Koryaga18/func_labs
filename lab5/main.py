def memoize(func):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = func(x) 
        return memo[x]
    return helper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))
