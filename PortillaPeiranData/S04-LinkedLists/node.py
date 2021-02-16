
class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    head: Node

    def __init__(self, head:Node):
        self.head = head
        self.tail = None
