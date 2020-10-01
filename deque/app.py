import collections

deke =  collections.deque()
deke.append(5)
deke.appendleft(6)
print(deke)
deke.pop()
print(deke)
deke.popleft()
deke.append(5)
print(deke)
