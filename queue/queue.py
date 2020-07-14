"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# from stack.stack import LinkedList,Node
class Node:
    def __init__(self,data,n=None):
        self.data = data
        self.next_node = n
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, val):
        self.next_node = val

    def get_data(self):
        return self.data

    def set_data(self,d):
         self.data = d     


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self,value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    
    def remove_head(self):
        if self.head is None and self.tail is None:
            return
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_data()   
        val = self.head.get_data()
        self.head = self.head.get_next()  
        return val

    def remove_tail(self):
         if self.head is None and self.tail is None:
            return

         if self.head is self.tail:
             value = self.head.get_data()
             self.head = None
             self.tail = None
             return value

         current = self.head

         while current.get_next() is not self.tail:
             current = current.get_next()

         val = self.tail.get_data()
         self.tail = current
         self.tail.next_node = None

         return val 

# Class Applied with LinkedList
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size +=1

    def dequeue(self):
        if self.size == 0:
            return
        else:    
            dequeue = self.storage.remove_head()
            self.size -=1
            return dequeue




















# Class applied with array
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.insert(0,value)
#         self.size = len(self.storage)

#     def dequeue(self):
#         if self.size == 0:
#             return
#         else:    
#             dequeue = self.storage.pop()
#             self.size = len(self.storage)
#             return dequeue

