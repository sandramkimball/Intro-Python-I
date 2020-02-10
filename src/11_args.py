# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.
def f1(int1, int2):
    return int1 + int2
print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the sum.
# Note: Google for "python arbitrary arguments" and look for "*args"
def f2(*argv):
    return sum(argv)
    
print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

# How do you have to modify the f2 call below to make this work?
a = [7, 6, 5, 4]
print(f2(a))

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the arguments.
# Note: Google "python default arguments" for a hint.
def f3(*argv):
    if len(argv) > 1:
        return sum(argv)
    else:
        return argv + 1

print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
# key: foo, value: bar
# Note: Google "python keyword arguments".
def f4(*kwargs):
    for key, value in kwargs:
        print(f(k: v))

f4(a=12, b=30)
f4(city="Berkeley", population=121240, founded="March 23, 1868")

# How do you have to modify the f4 call below to make this work?
d = {
    "monster": "goblin",
    "hp": 3
}
f4(d)
