numcalls = 0  # initialize numcalls to 0

def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x  # compute the square of x

print(square(2))  # call square the first time