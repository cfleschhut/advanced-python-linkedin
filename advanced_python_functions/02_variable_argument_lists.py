def addition(base, *args):
    print(base, args)
    return sum([base, *args])


print(addition(1, 2, 3))
print(addition(*[1, 2, 3]))
