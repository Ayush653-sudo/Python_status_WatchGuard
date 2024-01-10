class FirstHunderedGenerator:
    def __init__(self):
        self.number=0
    def __next__(self):
        if self.number<100:
            current=self.number
            self.number+=1
            return current
        else:
            raise StopIteration()
    def __iter__(self):
        return self
my_gen=FirstHunderedGenerator()
# print(next(my_gen))
# print(next(my_gen))

class FirstFiveIterator:
    def __init__(self):
        self.number=[1,2,3,4,5]
        self.i=0
    def __next__(self):
        if self.i<len(self.number):
            return self.number[self.i]

ite=FirstFiveIterator()

class AnotherIterable:
    def __init__(self):
        self.cars=['Fiat Linea','Thar']
    def __len__(self):
        return len(self.cars)
    def __getitem__(self, item):
        return self.cars[item]

my_number=[x for x in [1,2,3,4,5]]
my_number_gen=(x for x in [1,2,3,4])
print(next(my_number_gen))