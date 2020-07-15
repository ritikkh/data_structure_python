class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 0
    

class Avl(object):
    def __init__(self):
        self.root = None
        
    def calcHeight(self, node):
        if not node:
            return -1
        return node.height
    
    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcBalance(node.leftChild) - self.calcBalance(node.rightChild)
    
    def rightRotate(self, node):
        print("Rotating to the rght on node",node.data)
        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild
        tempLeftChild.rightChild = node
        node.leftChild = t
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1
        return tempLeftChild
    
    def leftRotate(self, node):
        print("Rotating to the left on node",node.data)
        tempRigtChild = node.rightChild
        t = tempRightChild.leftChild
        tempRightChild.leftChild = node
        node.rightChild = t
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1
        return tempRightChild    
    
    def insert(self, data):
        self.root = self.insertNode(data, self.root)
    
    def insertNode(self, data, node):
        if not node:
            return Node(data)
        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)        
        return self.settleViolation(data, node)
    
    def settleViolation(self, data, node):
        balance = self.calcBalance(node)
        
        #case : 1 left left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("left left heavy situation")
            return self.rightRotate(node)
        
        #case : 2 right right heavy situation
        if balance < -1 and data > node.rightChild.data:
            print("right right heavy situation")
            return self.leftRotate(node)
        
        #case : 3 lr situation
        if balance > 1 and data > node.leftChild.data:
            print("left right heavy situation")
            node.leftChild = self.leftRotate(node.leftChild)
            return self.rightRotate(node)
        
        #case : 4 rl situation
        if balance < -1 and data < node.rightChild.data:
            print("right left heavy situation")
            node.rightChild = self.rightRotate(node.rightChild)
            return self.leftRotate(node)
        return node
     
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)
            
    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
            
        print(node.data)
        
        if node.rightChild:
            self.traverseInOrder(node.rightChild)
            
avl = Avl()
avl.insert(5)
avl.insert(7)
avl.insert(6)

avl.traverse()
