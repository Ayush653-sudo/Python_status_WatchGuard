#
# def average_grade(student):
#     #pass
#     return sum(student['grades']/len(student['grades']))
# my_student = {
#     'name': 'Rolf',
#     'grades': [70, 80, 90, 99],
#     'average':"kk"
# }
# print(my_student)
# class Student:
#     def __init__(self,new_name,new_grades):
#         self.name=new_name
#         self.grades=new_grades
#     def average(self):
#         return sum(self.grades)/len(self.grades)
# student_one=Student('Ayush',[1,2,4,5])
# print(student_one.average())
# print(student_one.name)
# class Garage:
#     def __int__(self):
#         self.car=[]
#
#     def __len__(self):
#         return len(self.car)
#
#     def __getitem__(self,i):
#         return self.car[i]
#     def __repr__(self):
#         return f'<Garage {self.car}>'
#     def __str__(self):
#         return f'Garage with {len(self)} cars.'
# ford=Garage()
# ford.car.append('Fiesta')
# ford.car.append('Focus')
# for car in ford:
#     print(car)
class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object=Foo()
print(Foo.hi())
class Bar:
    @staticmethod
    def hi():
        print('Hello,I do not take argument')

    @staticmethod
    def from_sum(value1, value2):
        return value1 + value2
another_object=Bar()
another_object.hi()
print(Bar.from_sum(1,2))