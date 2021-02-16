from PortillaPeiranData.S03_StacksQueuesDeques.deque import Deque

d = Deque()

print(d.is_empty())

d.addFront('Martin')
d.addRear('Rose')

print(d.removeFront())
print(d.removeRear())

print(d.size())

