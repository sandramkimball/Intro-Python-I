# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
# This will print 12. What do we have to modify in change_x() to get it to print 99?
x = 12
def change_x(x):
    x = 99
    
change_x(x)
print(x)


# This nested function has a similar problem.
# This prints 120. What do we change in inner() to print 999?
# Note: Google "python nested function scope".
def outer():
    y = 120
    def inner(y):
         y = 999
    return inner(y)
outer()
print(y)