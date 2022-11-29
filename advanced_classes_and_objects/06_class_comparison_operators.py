class Employee:
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority

        return self.level > other.level

    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority

        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority

        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority

        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level


dept = [
    Employee("Tim", "Sims", 5, 9),
    Employee("John", "Doe", 4, 12),
    Employee("Jane", "Smith", 6, 6),
    Employee("Rebecca", "Robinson", 5, 13),
    Employee("Tyler", "Durden", 5, 12)
]

print(dept[3] >= dept[4])

for employee in sorted(dept):
    print(f"{employee.fname} {employee.lname}, {employee.level} {employee.seniority}")
