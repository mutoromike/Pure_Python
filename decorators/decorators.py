"""
    A decorator is a higher order function that takes a function as an
    argument and returns a closure (the enclosed function).
"""


def greeting_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Greetings! {result}"

    return wrapper


"""
    The @greeting_decorator is the same as:
    my_function = greeting_decorator(my_function)

    The wrapper function is the closure that is returned by the decorator.
"""


@greeting_decorator
def my_function():
    return "Hello, World!"


print(my_function())
# Greetings! Hello, World!
