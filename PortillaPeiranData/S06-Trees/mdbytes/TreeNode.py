class TreeNode:

    def __init__(self, key, val,left=None,right=None,parent=None):
        """
        Initiates new nodes for the binary search tree.  Default values for
        parent, left child, and right child, are None.
        """
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    # returns child if exists
    def hasLeftChild(self):
        return self.leftChild

    # returns child if exists
    def hasRightChild(self):
        return self.rightChild

    # returns true if node is left child of a parent
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    # returns true if node is right child of a parent
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    # returns true if node is root (has no parent)
    def isRoot(self):
        return not self.parent

    # returns true if node is leaf (on last layer of tree)
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    # returns true if node has any children
    def hasAnyChildre(self):
        return self.rightChild or self.leftChild

    # returns true if node has both children
    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    # replaces node data
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

