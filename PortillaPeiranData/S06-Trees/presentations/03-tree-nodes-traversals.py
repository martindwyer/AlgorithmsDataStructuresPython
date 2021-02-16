class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self, obj):
        self.key = obj

    def getRootValue(self):
        return self.key


def preOrder(tree):
    if tree:
        print(tree.getRootValue())
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())

def postOrder(tree):
    if tree:
        postOrder(tree.getLeftChild())
        postOrder(tree.getRightChild())
        print(tree.getRootValue())

def inOrder(tree):
    if tree:
        inOrder(tree.getLeftChild())
        print(tree.getRootValue())
        inOrder(tree.getRightChild())



"""
Constructing the binary tree 
"""
r = BinaryTree(0)
print(r.getRootValue())

r.insertLeft('1')
r.insertRight('a')

r.getLeftChild().insertLeft(2)
r.getLeftChild().insertRight(3)

r.getRightChild().insertLeft('b')
r.getRightChild().insertRight('c')
r.getRightChild().getRightChild().insertLeft('d')
r.getRightChild().getRightChild().insertRight('e')

print(r.getLeftChild().getRootValue())
print(r.getRightChild().getRootValue())

"""
Traversals
"""
print('\npreorder traversal; 1) root, 2) left sub, 3) right sub')
preOrder(r)

print('\npostorder traversal; 1) left sub, 2) right sub, 3) root')
postOrder(r)

print('\ninorder traversal; 1) left sub, 2) root, 3) right sub')
inOrder(r)
