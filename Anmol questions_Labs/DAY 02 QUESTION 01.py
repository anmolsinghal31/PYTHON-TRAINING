# Q2: Custom Iterator Class
class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


# Q2: Generator Function
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Q3: Demonstration
def demonstrate():
    N = 5

    print(f"Q1:Custom Iterator (1 to {N})")
    it_obj = NumberIterator(N)
    for num in it_obj:
        print(num, end=" ")
    print("\n")

    print(f"Q2:Generator Function (First {N} Fibonacci)")
    gen_obj = fibonacci_generator(N)
    for fib in gen_obj:
        print(fib, end=" ")
    print("\n")

    print("Q3: Key Differences ")
    print("1. Syntax: The Iterator uses a class; the Generator uses a simple function.")
    print("2. State: The Iterator manually tracks 'self.current'; the Generator saves state automatically via 'yield'.")
    print("3. Code: Generators are much more concise and memory-efficient for simple tasks.")


if __name__ == "__main__":
    demonstrate()