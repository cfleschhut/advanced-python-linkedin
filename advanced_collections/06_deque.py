from collections import deque
from string import ascii_lowercase

d = deque(ascii_lowercase)
print(len(d))

d.pop()
d.popleft()

d.append(2)
d.appendleft(1)

print(d)
d.rotate(3)
d.rotate(-2)
print(d)
