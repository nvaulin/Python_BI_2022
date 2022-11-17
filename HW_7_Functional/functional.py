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




def multiple_partial():
    pass


def my_print():
    pass
