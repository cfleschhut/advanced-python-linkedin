class Person:
    def __init__(self):
        self.fname = "Firstname"
        self.lname = "Lastname"
        self.age = 99

    def __repr__(self):
        return f"{self.fname} {self.lname}, {self.age}"

    def __str__(self):
        return f"Person ({self.fname} {self.lname}, {self.age})"

    def __bytes__(self):
        return bytes(f"Person ({self.fname} {self.lname}, {self.age})".encode("utf-8"))


person = Person()

print(repr(person))
print(str(person))
print(f"{person}")

print(bytes(person))
