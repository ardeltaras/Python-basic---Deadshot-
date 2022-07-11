        # 1. Implement class iterator for Fibonacci numbers
        # https://en.wikipedia.org/wiki/Fibonacci_number
        # Iterator get numbers of first Fibonacci numbers
print("\n#---1---#")

class FibonacciNumbers:
    def __init__(self, quantity, step=1):
        self.quantity = quantity
        self.step = step
        self.iter = 0
        self.previous = 0 - step
        self.current = 1
        self.next = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter > self.quantity:
            raise StopIteration
        self.iter += 1
        self.next = self.previous + self.current
        self.previous = self.current
        self.current = self.next
        return self.next

for i in FibonacciNumbers(10):
    print(i)


        # 2.
        # Implement generator for Fibonacci numbers
print("\n#---2---#")

def gen_fibonacci(quantity):
    previous = 0
    current = 1
    next = 1
    for gen in range(quantity):
        yield next
        next = previous + current
        previous = current
        current = next

for i in gen_fibonacci(10):
    print(i)


        # 3.
        # Write generator expression that returns square numbers of integers from 0 to 10
print("\n#---3---#")

def gen(numbers):
    for num in range(numbers):
        yield num ** 2

for i in gen(10):
    print(i)


        # 4.
        # Implement coroutine for accumulation arithmetic mean
print("\n#---4---#")

def accumulation_mean():
    acc = 0
    count = 0
    mean = 0
    while True:
        current = yield mean
        acc += current
        count += 1
        mean = acc//count

acc_mean = accumulation_mean()
next(acc_mean)
print(acc_mean.send(2))
print(acc_mean.send(8))
print(acc_mean.send(2))
print(acc_mean.send(4))