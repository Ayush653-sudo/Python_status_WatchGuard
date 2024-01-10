from collections import defaultdict
from collections import OrderedDict
cowerkers=[('Rolf','MIT'),('JEN','Oxford')]
other_coworker=[('Rolf','Apple Inc.'),('Anna','Google')]
alma_maters=defaultdict(list)
for cowerker,place in cowerkers:
    alma_maters[cowerker].append(place)

#alma_maters.default_factory=None#To make it null
my_company='Teclado'
coworker_companies=defaultdict(lambda:my_company)
for person,companies in other_coworker:
    coworker_companies[person]=my_company

print(coworker_companies[cowerker[0]])
print(coworker_companies['Rolf'])
o=OrderedDict()
o['Rolf']=6
o['Jose']=12
o['Jen']=3
print(o)
o.move_to_end('Rolf')
o.move_to_end('Jen',last=False)
print(o)