my_file=open('data.txt','r')
file_content=my_file.read()
my_file.close()
print(file_content)
user_name=input('Enter ')
friends=input("Enter three friend names, separated by comas (no spaces,please): ").split(',')
people=open('Data.txt','r')
people_nearby=[line.strip() for line in  people.readlines()]
people.close()
friends_set=set(friends)
friends_nearby_set=set(people_nearby)
friend_nearby=friends_nearby_set.intersection(friends_set)
nearby_friends_file=open('nearby_friend.txt','w')
for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()