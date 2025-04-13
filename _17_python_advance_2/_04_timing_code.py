from timeit import timeit

# a: str = 'list(range(1000))'
# b: str = 'set(range(1000))'
# # We used warnup to make the interpreter run at full speed
# warnup: float = timeit(stmt=a, number=100_000)
# a_time: float = timeit(stmt=a, number=100_000)
# b_time: float = timeit(stmt=b, number=100_000)
# print(f'a: {a_time:.3f} sec')
# print(f'b: {b_time:.3f} sec')


# # But we can also use repeat to run the code multiple times and this does not require a warmup since multiple repetitions make the interpreter run at full speed
# a: str = 'list(range(1000))'
# b: str = 'list(range(1000))'
# c: str = 'set(range(1000))'
# a_time: float = min(repeat(stmt=a, repeat=5, number=100_000))
# b_time: float = min(repeat(stmt=b, repeat=5, number=100_000))
# c_time: float = min(repeat(stmt=c, repeat=5, number=100_000))
# print(a_time)
# print(b_time)
# print(c_time)


# Here we are using the timeit function to measure the time it takes to run a piece of code by ** and math.pow
power_time: float = timeit("a*b", setup='a,b = 10,3')
print(f'a**b: {power_time:.3f} sec')
math_power_time: float = timeit(stmt='pow(10,3)',
                                setup='from math import pow')  # We can also use triple quotes for the setup
print(f'pow(10,3): {math_power_time:.3f} sec')
