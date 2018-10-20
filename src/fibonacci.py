# returns N's fibonacci number
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    n1 = 0
    n2 = 1
    current = 1
    current_value = 0
    while current < n:
        current_value = n1 + n2
        n1 = n2
        n2 = current_value
        current += 1
    return current_value


print(fib(4))
