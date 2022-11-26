nums = (0, 1, 2, 3, 4, 5)
chars = ('a', 'A', 'b', 'B', 'c', 'C')

odds = filter(lambda num: not num % 2 == 0, nums)
print(list(odds))

lowers = filter(lambda c: not c.isupper(), chars)
print(list(lowers))

squares = map(lambda num: num ** 2, nums)
print(list(squares))
