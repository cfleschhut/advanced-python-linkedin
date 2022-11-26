b = bytes([0x41, 0x42, 0x43, 0x44])
# print(b)

s = "This is a string"
# print(s)


def decodeBytes():
    print(s + b.decode("utf-8"))


decodeBytes()


def encodeStrings():
    print(b + s.encode("utf-8"))
    print(s.encode("utf-32"))


encodeStrings()
