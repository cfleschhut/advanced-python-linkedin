def myFunction(arg1, arg2=None):
    """Print given arguments.

    Arguments:
    arg1: Anything
    arg2: Anything (default None)
    """

    print(arg1, arg2)


myFunction("a", "b")
print(myFunction.__doc__)
