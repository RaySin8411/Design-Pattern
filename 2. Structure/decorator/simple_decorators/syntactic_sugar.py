import functools


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def say_wheel():
    print("Wheel!")


@do_twice
def greet(name):
    print(f"Hello {name}")


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


if __name__ == '__main__':
    say_whee()
    say_wheel()
    greet("World")
    hi_adam = return_greeting("Adam")
    print(hi_adam)
