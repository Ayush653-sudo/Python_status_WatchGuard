def hundered_numbers():
    i=0
    while i<100:
        yield i
        i+=1
g=hundered_numbers()
print(next(g))
my_range_obj=range(10)

