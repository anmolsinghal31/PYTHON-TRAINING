def add(a, b):
    print(a + b)


def sub(a, b):
    return a - b, a


add(1, 2)
print(sub(3, 4))


def hello(greeting="Hello", name="world"):
    print('%s,%s' % (greeting, name))


hello()
hello('greetings', 'anmol')


def print_param(*params):
    print(params)


def print_params(**params):
    print(params)


print_param('Testing')
print_param(1, 2, 3)

def print_param1(**params):
    print(params)

print_param1(x=2, y=3)

