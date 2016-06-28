"""Demo Module"""


def nice_function(value):
    return value**2


def bad_code(bar):
    foo = bar*2
    xyz = 500
    return foo

if __name__ == "__main__":
    print("Hello Sputnik!")
    print(nice_function(5))
    print(bad_code(10)) 
