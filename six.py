def add(a, b):
    return a + b

print(add(3, 4))

def subtract(a, b):
    return a - b
print(subtract(10, 5))

def name(name):
    return "Hello, " + name
print(name("Alice"))

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)   

print(recursive_factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1, 6):
    print(fibonacci(i), end=" ")


