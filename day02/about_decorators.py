def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"


def greet_with(greeter_func):
    return greeter_func("Bob")

#greet_with(say_hello)

#greet_with(be_awesome)

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = decorator(say_whee)
