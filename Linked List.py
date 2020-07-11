#Linked List Implementation
class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    # O(1)
    def insertStart(self, data):
        self.size = self.size +1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    #O(1)        
    def size1(self):
        return self.size
    
    #O(N)--Not a good way
    def size2(self):
        actualNode = self.head
        size = 0
        
        while actualNode is not None:
            size+=1
            actualNode = actualNode.nextNode
        return size
    # O(N)--it is expensive than insertion at start    
    def insertEnd(self, data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode
    #O(N)    
    def traverse(self):
        actualNode = self.head
        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode
    #O(N)        
    def remove(self, data):
        if self.head is None:
            return
        self.size -= 1
        prevNode = None
        currNode  =self.head
        while currNode.data != data:
            prevNode = currNode
            currNode = currNode.nextNode
        if prevNode is None:
            self.head = currNode.nextNode
        else:
            prevNode.nextNode = currNode.nextNode 
        
ll = LinkedList()
ll.insertStart(0)
ll.insertStart(1)
ll.insertStart(2)
ll.insertStart(3)
ll.remove(3)
ll.traverse()
ll.size2()
