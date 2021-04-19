import math

def func_max(f, g):
    def h(x):
        return max(f(x), g(x))
    return h

def double(x):
    return 2*x

def square(x):
    return x*x

h1 = func_max(double, square)

print(h1(1) == 2 )
print("must be True")
print(h1(3) == 9)
print("must be True")
h2 = func_max(double, abs)
#abs is standard Python function computing absolute value of number
print(h2(-2) == 2)
print("must be True")