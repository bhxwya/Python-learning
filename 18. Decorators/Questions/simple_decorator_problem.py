def uppercase(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result.upper())

    return wrapper


@uppercase
def greet(name):
    return f"Hello, {name}!"


greet("ansh")