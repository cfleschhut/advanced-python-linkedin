from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()


print(Fruit.APPLE)
print(type(Fruit.APPLE))
print(repr(Fruit.APPLE))
print(Fruit.APPLE.name, Fruit.APPLE.value)

print(Fruit.PEAR.value)

fruits = {}
fruits[Fruit.BANANA] = "banana"
print(fruits[Fruit.BANANA])
