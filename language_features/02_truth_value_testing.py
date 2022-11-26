class MyClass:
    pass
    # def __bool__(self):
    #     return False

    # def __len__(self):
    #     return 0


my_class = MyClass()

print("Truthy") if my_class else print("Falsy")
print(bool(my_class))

print(bool([]))
print(bool({}))
