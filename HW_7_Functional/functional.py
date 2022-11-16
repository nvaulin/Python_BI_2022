import sys


def sequential_map(*args):
    args = [*args][::-1]
    container = args.pop(0)
    while args:
        container = list(map(args.pop(), container))
    return container


def consensus_filter(*args):
    args = [*args][::-1]
    container = args.pop(0)
    while args:
        container = list(filter(args.pop(), container))
    return container


def conditional_reduce(func_1, func_2, container):
    container = filter(func_1, container)
    result = sequential_map(func_2)
    while container:
        result +=
    return result


def func_chain():
    pass


def multiple_partial():
    pass


def my_print():
    pass


