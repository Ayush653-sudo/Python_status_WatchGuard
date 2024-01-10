from collections import deque
friend=deque(('Rolf','Chrlie','Jen','Anna'))
friend.append('Jose')
friend.appendleft('Anthony')
friend.pop()
friend.popleft()
print(friend)