def myFunction(arg1, arg2, *, kwArg1, kwArg2):
    print(arg1, arg2, kwArg1, kwArg2)


# myFunction(1, 2, True, True)
myFunction(1, 2, kwArg1=True, kwArg2=True)
