import itertools

seq1 = ["A", "B", "C"]


def cycle():
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1), end=" ")
    print(next(cycle1), end=" ")
    print(next(cycle1), end=" ")
    print(next(cycle1))


cycle()


def count():
    count1 = itertools.count(100, 10)
    print(next(count1), end=" ")
    print(next(count1), end=" ")
    print(next(count1), end=" ")
    print(next(count1))


count()


def accumulate():
    vals = [10, 20, 30, 40, 50, 10, 20]
    # acc = itertools.accumulate(vals)
    acc = itertools.accumulate(vals, max)
    print(vals, list(acc))


accumulate()


def chain():
    print(list(itertools.chain(["a", "b"], [1, 2], ["c", "d"], [3, 4])))


chain()


def dropTakeWhile():
    vals = [10, 20, 30, 40, 50, 40, 10]

    print(list(itertools.takewhile(lambda num: num < 40, vals)))
    print(list(itertools.dropwhile(lambda num: num < 40, vals)))


dropTakeWhile()
