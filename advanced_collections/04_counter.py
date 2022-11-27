from collections import Counter

class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah"
          "Kevin", "James", "James", "Melanie", "Penny", "Steve"]
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

c1 = Counter(class1)
c2 = Counter(class2)

print(c1["James"])
print(sum(c1.values()))

c1.update(class2)
print(sum(c1.values()))

print(c1.most_common(3))

c1.subtract(class2)
print(c1.most_common(3))

print(c1 & c2)
