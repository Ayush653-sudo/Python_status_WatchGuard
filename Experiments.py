def val():
    stream = "ff"
class CSStudent:
    stream = 'cse'

    def __init__(self, name, roll):

        self.name = name
        self.roll = roll
    @staticmethod
    def val():
        stream="ff"
    @classmethod
    def change(cls):
        cls.stream="ff"


# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)
print(CSStudent.stream)
CSStudent.change()
print(CSStudent.stream)
print(b.stream)

