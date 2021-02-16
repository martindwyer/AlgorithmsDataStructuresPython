from PortillaPeiranData.S03_StacksQueuesDeques.stack import Stack

class Queue(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,item):
        self.stack1.push(item)

    def dequeue(self):
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())

        answer = self.stack2.pop()

        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.pop())

        return answer


"""
RUN THIS CELL TO CHECK THAT YOUR SOLUTION OUTPUT MAKES SENSE AND BEHAVES AS A QUEUE
"""
q = Queue()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())