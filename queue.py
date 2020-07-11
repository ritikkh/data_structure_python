class Queue(object):
    def __init__(self):
        self.queue = []
        
    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def sizeQueue(self):
        return len(self.queue)
    
    def peek(self):
        return self.queue[0]
    
    def isEmpty(self):
        return self.queue == []
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.sizeQueue()
q.dequeue()
q.peek()