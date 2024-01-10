l=1,2,3
print(type(l))
art_frien={"Rolf","Anne","Jen"}
science_friend={"Jen","Charlie"}
not_in_both=art_frien.symmetric_difference(science_friend)
science_but_not_art=art_frien.difference(science_friend)
print(not_in_both)
print(science_but_not_art)
lk=[12.3]
friend_age={"Rolf":254,"Adam":30,"Anne":35,"Rolf":45}
print(friend_age)
friends=["Rolf","Anne","Charlie"]
comma_separated=",".join(friends)
print(f"My friends are {comma_separated}")
for f in friends:
   # friends.append("Mack")
    print(f)
for name,age in friend_age.items():
    print(f"{name}is {age} years old.")
times_since_seen=[3,7,15,11]
long_timers=list(zip(friends,times_since_seen,[1,2,3,4,5]))
print(long_timers)
for counter, friend in enumerate(friends,start=1):
    print(counter)
    print(friend)
print(list(enumerate(friends)))
print(dict(enumerate(friends)))
