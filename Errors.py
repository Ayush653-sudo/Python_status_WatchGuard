#Different types of error in python

#Index Error->index out of range
#KeyError=>like trying to access the key which is not present
#NameError->when using variale which is not present
#AttributeError->if some object do not have particular attribute which you are trying to invoke
#NotImplementedError
#RuntimeError
#SyntaxError
#IndentationError
#TabError
#TypeError
#ValueError
#importError->Circular Error

range_key_dict = RangeKeyDict({
        (0, 100): 'A',
        (100, 200): 'B',
        (200, 300): 'C',
    })
class Garage:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def __repr__(self):
        return f'<Car{self.make}'
    def __len__(self):
        return len(self.cars)
    def add_car(self,car):
        raise NotImplementedError("We can;t add cars to the garage yet.")
a=10
ford=Garage("c","s")

try:
    ford.add_car('Fiesta')
except TypeError:
    print('your can was not able to add')
else:
    print("this will only execute if our try block will pass")
finally:
    print('this section will going to be execute always')

print(len(ford))


class MyCustomError(TypeError):
    def __init__(self,message,code):
        super().__init__(message)
        self.code=code
raise MyCustomError('OUCH!An Error Happened',500)
#from range_key_dict import RangeKeyDict

