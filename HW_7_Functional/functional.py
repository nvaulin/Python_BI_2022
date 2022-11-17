import sys

# Дополнительная функция для заданий 1 и 2 т.к. их две функции были слишком похожи чтобы не объединить в одну
def sequential_apply(method, *args):
    args = [*args][::-1]
    container = args.pop(0)
    while args:
        container = list(method(args.pop(), container))
    return container


# Задание 1
def sequential_map(*args):
    """
    The function takes several functions and a container with data,
    after which it sequentially applies the functions to each element of the container separately

    Input:
        python functions \n
        container of objects

    Output:
        container of objects of sequential functions application
    """
    return sequential_apply(map, *args)


# Задание 2
def consensus_filter(*args):
    """
The function takes several filtering functions (bool-outputing) and a container with data,
after which it sequentially applies the filters to each element of the container and returns
a values passed all the filterings

Input:
    python bool-outputing functions \n
    container of objects

Output:
    container of objects passed all the filterings
"""
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


def my_print(*objects, sep=' ', end='\n', file=None):
    objetcs = list(map(str, objects))
    output = sep.join(objetcs) + end
    if file:
        sys.stdout = open(file, "w")
    sys.stdout.write(output)
