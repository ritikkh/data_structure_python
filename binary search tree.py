class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)
            
    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)
                
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
    
    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data
    
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
    
    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        return node.data
    
    def traverse(self):
        if self.root:
            return self.traverseInOrder(self.root)
        
    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
            
        print(node.data)
        
        if node.rightChild:
            self.traverseInOrder(node.rightChild)
            
    def remove(self, data):
        if self.root:
            return self.removeNode(data, self.root)
        
    def removeNode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("removing leaf node....")
                del node
                return None
            if not node.leftChild:
                print("removing the node with single right child...")
                temp = node.rightChild
                del node
                return temp
            elif not node.rightChild:
                print("removing the node with single left child...")
                temp = node.leftChild
                del node
                return temp
            print("removing the node with two child")
            temp = self.getPredecessor(node.leftChild)
            node.data = temp.data
            node.leftChild = self.removeNode(temp.data, node.leftChild)
        return node
            
    def getPredecessor(self, node):
        if node.rightChild:
            return getPredecessor(node.rightChild)
        return node
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(14)
bst.insert(6)          
bst.traverse()            
bst.remove(10)