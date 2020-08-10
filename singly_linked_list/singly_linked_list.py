class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self,value):
        node = Node(value)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head = node
    def add_to_tail(self, value):
        node = Node(value)
        if self.tail is None and self.head is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
    
    def remove_head(self):
        # we have to make the value next to the head the 
        # the new head of the list
        current_next = self.head.next

        if self.head is self.tail:
            self.head.value = None
            self.tail.value = None
        else:
            # self.head = None
            self.head = current_next
    
    def contains(self,value):
        start = self.head
        while (start is not None):
            if start.value == value:
                return value
            start = start.next   
                     
                

