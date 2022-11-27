ctemps = [0, 12, 34, 100]
ftemps = [32, 65, 100, 212]


def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9


print(list(map(CelsisusToFahrenheit, ctemps)))
print(list(map(FahrenheitToCelsisus, ftemps)))

print(list(map(lambda temp: (temp * 9/5) + 32, ctemps)))
print(list(map(lambda temp: (temp-32) * 5/9, ftemps)))
