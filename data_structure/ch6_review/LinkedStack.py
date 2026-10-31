from Node import Node


class LinkedStack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None
    
    def isFull(self):
        return False
    
    def push(self,item):
        n = Node(item,self.top)
        self.top = n
        
    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
        
    def peek(self):
        if not self.isEmpty():
            return self.top.data
        
    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
            
        return count
    
    def __str__(self):
        arr = []
        node = self.top
        while not node == None:
            arr.append(node.data)
            node = node.link
        return str(arr)