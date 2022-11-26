days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
daysFr = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]


def iterators():
    i = iter(days)

    print(next(i))
    print(next(i))
    print(next(i))


iterators()


def readFile():
    with open("testfile.txt", "r") as fp:
        for line in iter(fp.readline, ""):
            print(line)


readFile()


def enumerateDays():
    for i, day in enumerate(days, start=1):
        print(i, day)


enumerateDays()


def combineDays():
    for d in zip(days, daysFr):
        print(f"{d[0]} = {d[1]}")


combineDays()
