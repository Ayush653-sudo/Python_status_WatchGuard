
ranges_value = [(0, 10, 5), (11, 20, 9), (21, 30, 90)]
lookup = {}
for min_val, max_val, value in ranges_value:

    lookup.update(dict.fromkeys(range(min_val, max_val + 1), value))




a=20.12
b=str(a)
b=b.split('.')
print(lookup[int(b[1])])
#
#
#
# ranges_value = [(0, 10 ,1), (11, 20,2), (21, 30,3)]
# lookup={}
#
# for i,(min_val, max_val,value) in enumerate(ranges_value):
#     lookup.fromkeys(range(min_val, max_val + 1),value)
#
# print(lookup[1])
# ranges_value = [(0, 10, 1), (11, 20, 2), (21, 30, 3)]
# lookup = {}
#
# for min_val, max_val, value in ranges_value:  # No need for enumerate here
#     for i in range(min_val, max_val + 1):  # Iterate through each value in the range
#         lookup[i] = value  # Assign the value to the corresponding key in the lookup
#
# print(lookup[1])  # This will now correctly print 1
