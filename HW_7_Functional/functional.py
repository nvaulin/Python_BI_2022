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
    """
    Applies filter and 2-valued 1-value-returning function to reduce a container.

    Input:
        python filtering function\n
        python reducing function (takes 2 values, returns 1)\n
        container

    Output:
        single value
    """
    container = list(filter(func_1, container))[::-1]
    while len(container) > 1:
        container.append(func_2(container.pop(), container.pop()))
    return container.pop()


# Задаение 4
def func_chain(*funcs):
    """
    Takes any number of functions and turns them into a single pipeline function

    Input:
        several python functions

    Output:
        single function
    """
    funcs = [*funcs][::-1]

    def pipe(*args):
        arguments = list(args)
        while funcs:
            arguments = list(map(funcs.pop(), arguments))
        # map спрятан в наружний список, если там 1 значение решил достать результат из него по-функциональному
        result = (lambda x: x)(*arguments) if len(arguments) == 1 else arguments
        return result

    return pipe


# Интеграция func_chain в задание 1
def sequential_map_2(*args):
    args = list(args)
    container = args.pop()
    pipe = func_chain(*args)
    return pipe(*container)


def multiple_partial(*args, **kwargs):
    """
    Takes several functions and arguments and passes the given arguments to the functions in advance.
    When called, all functions will be updated with new arguments and the results of the functions will be eaten out as a list
    """
    funcs, arguments = [], []
    # Separation of *args into function and arguments for functions
    for arg in args:
        (funcs if callable(arg) else arguments).append(arg)

    def multitool(*_args):
        results = []
        arguments.extend(list(_args))
        for f in funcs:
            results.append(f(*arguments, **kwargs))
        return results

    return multitool


def my_print(*objects, sep=' ', end='\n', file=None):
    """
    The function allows you to display variables in the console
    (or in a file, if specified) without calling the print function!

    Input:
        several objects to display

    Parameters:
        sep (str): separator of objects
        end (str): ending symbol
        file (str): path to file to write (optional)

     Output:
        string of given variables in standard output (console or file)
    """
    objects = list(map(str, objects))
    output = sep.join(objects) + end
    if file:
        sys.stdout = open(file, "w")
    sys.stdout.write(output)
