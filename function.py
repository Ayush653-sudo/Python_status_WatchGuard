car=[{"make":"Ford","model":"fiesta","mileage":2300},
     {"make":"Ford","model":"focus","mileage":2305}
     ]
def car_name(car):
    print(car)

def multiple(*args):
    print(*args)

car_name(car)
multiple([1,2,3],4,5)
avg=lambda seq:sum(seq)/len(seq)
total=lambda seq:sum(seq)
top=lambda seq:max(seq)
operations={
    "average":avg,
    "total":total,
    "top":top
}
students=[
    {"name":"Rolf","grades":(6,90,95,100)}
]
for student in students:
    name=student["name"]
    grades=student["grades"]
    print(f"Student: {name}")
    operation=input("Enter choics")
    operation_function=operation[operation]
    print(operation_function(grades))
