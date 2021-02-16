"""
See Miller and Raynum
pp. 128 to 142
"""

class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self,new_data):
        self.data=new_data

    def set_next(self,new_next):
        self.next = new_next

class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self,data):
        temp = Node(data)        # new node with the new data
        temp.set_next(self.head) # put new node after current head
        self.head = temp         # set new node as head

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == data:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self,data):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

