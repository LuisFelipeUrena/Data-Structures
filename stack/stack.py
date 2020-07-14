"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
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
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size


    def push(self,value):
        self.storage.add_to_tail(value)
        self.size +=1

    def pop(self):
        if self.size == 0:
            return None
            
        else:
            popped = self.storage.remove_tail()
            self.size -=1
            return popped                 




# Class Applied with Array(python list)
# class Stack:
#     def __init__(self, head=None):
#         self.storage = 0
#         self.head = head
#         self.foot = None




# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size


#     def push(self,value):
#         self.storage.append(value)
#         self.size = len(self.storage)

#     def pop(self):
#         if self.size == 0:
#             return None
            
#         else:
#             popped = self.storage.pop() 
#             self.size = len(self.storage)
#             return popped                 



# class Stack:
#     def __init__(self, head=None):
#         self.storage = 0
#         self.head = head
#         self.foot = None
        

#     def __len__(self):
#         return self.storage

#     def push(self, value):
#         new_node  = Node(value,self.head.get_next())
#         if self.head == None:
#             self.head = new_node
#             self.storage += 1
#         else:
#             return    

        

#     def pop(self):
#         this_node = self.head
        
        
#         self.head = Node(this_node.get_next())
#         self.storage -= 1 
