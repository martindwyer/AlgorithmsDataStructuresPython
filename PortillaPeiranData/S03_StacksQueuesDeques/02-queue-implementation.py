
from PortillaPeiranData.S03_StacksQueuesDeques.queue import Queue

q = Queue()

q.enqueue('Kyle')
q.enqueue('Casey')
q.enqueue('Noah')

print(q.size())

print(q.dequeue())

print(q.size())