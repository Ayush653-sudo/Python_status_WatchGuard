

def starts_with_r(friend):
    return friend.startswith('R')
friends=['Rolf','Jose','Ayush']
start_with_r=filter(starts_with_r,friends)
# print(next(start_with_r))
# print(next(start_with_r))
print(list(start_with_r))
print(list(start_with_r))
def my_custom_filter(func,iterable):
    for i in iterable:
        if func(i):
            yield i
#Generator compression
#List Compression
start_with_r=my_custom_filter(lambda friend:friend.startswith('R'),friends)
friends_lower=map(lambda x:x.lower(),friends)

class User:
    def __inti__(self,username,password):
        self.username=username
        self.password=password
    @classmethod
    def from_dict(cls,data):
        return cls(data['username'],data['password'])

users=[

    {
        'username':'rolf',
        'password':'123'
    },
    {
        'username':'tecaladoisawsome',
        'password':'youaretoo'
    }
]
users=[User.from_dict(user) for user in users]
users=map(User.from_dict,users)
friends=[

    {
        'name':'rolf',
        'location':'noida'
    },
    {
        'name':'Jose',
        'location':'kota'
    }
]
your_location=input('Where are you right now?')
friend_nearby=[friend for friend in friends if friend['location']==your_location]
if any(friend_nearby):
    print('you are not alone')
print(all([0,1,3,4]))

