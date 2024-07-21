def fibonacci(n):
    """function to recursively calculate the nth term of
    fibonacci series

    Args:
        n (int): the target term to be returned

    Returns:
        int: returns the nth term of fibonacci series
    """
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
