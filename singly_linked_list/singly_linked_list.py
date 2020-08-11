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
        if self.head is None and self.tail is None:
            return
        if not self.head.next:
            head = self.head
            self.head = None
            self.tail = None
            return head.value  
        val = self.head.value
        self.head = self.head.next  
        return val
    
    def contains(self,value):
        start = self.head
        while (start is not None):
            if start.value == value:
                return value
            start = start.next  

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value          

