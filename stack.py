class Stack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack.append(data)
        
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return self.stack == []
    
    def stackSize(self):
        return len(self.stack)
    
st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.peek()
st.pop()
st.isEmpty()
st.stackSize()