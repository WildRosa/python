import logging
logging.basicConfig(level=logging.INFO)


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


while True:
    m = int(input())
    res = fibonacci(m)
    logging.info('%s', res)
