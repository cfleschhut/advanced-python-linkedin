from collections import defaultdict

fruits = ['apple', 'pear', 'orange', 'banana',
          'apple', 'grape', 'banana', 'banana']

# fruitCounter = defaultdict(int)
fruitCounter = defaultdict(lambda: 100)

for fruit in fruits:
    fruitCounter[fruit] += 1

for key, value in fruitCounter.items():
    print(f"{key}: {value}")
