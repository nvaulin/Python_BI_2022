import sys
import numpy as np


# Дополнительная функция для заданий 1 и 2 т.к. их две функции были слишком похожи чтобы не объединить в одну
def sequential_apply(method, *args):
    args = [*args][::-1]
    container = args.pop(0)
    while args:
        container = list(method(args.pop(), container))
    return container


# Задание 1
def sequential_map(*args):
    return sequential_apply(map, *args)


# Задание 2
def consensus_filter(*args):
    return sequential_apply(filter, *args)


# Задание 3
def conditional_reduce(func_1, func_2, container):
    container = list(filter(func_1, container))[::-1]
    while len(container) > 1:
        container.append(func_2(container.pop(), container.pop()))
    return container.pop()


# Задаение 4
def func_chain(*funcs):
    funcs = [*funcs][::-1]

    def pipe(*args):
        arguments = list(args)
        while funcs:
            arguments = list(map(funcs.pop(), arguments))
        # map спрятан в наружний список, если там 1 значение решил достать результат из него по-функциональному
        result = (lambda x: x)(*arguments) if len(arguments) == 1 else arguments
        return result

    return pipe


# Интеграция func_chain в 1 задание
def sequential_map_2(*args):
    args = list(args)
    container = args.pop()
    pipe = func_chain(*args)
    return pipe(*container)


def multiple_partial(*args, **kwargs):
    funcs, arguments = [], []

    # Separation of *args into function and arguments for functions
    for arg in args:
        (funcs if callable(arg) else arguments).append(arg)

    def multitool(*args):
        results = []
        arguments.extend(list(args))
        for f in funcs:
            results.append(f(*arguments, **kwargs))
        return results

    return multitool


my_print = multiple_partial(print, "Hello", sep=", ", end=".....")
print(my_print("Username", "this is functools tutorial"))
my_stat = multiple_partial(np.mean, np.max, np.sum, axis=1)
print(my_stat([[1, 2], [1, 2]]))


def my_print():
    pass
