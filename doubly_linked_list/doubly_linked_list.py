"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node  = ListNode(value)
        if self.head is None:
            new_node.next = self.head
            new_node.prev = None
        else:
            self.head.prev = new_node
        
        self.head = new_node        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        current_node  = self.head
        self.head = current_node.next
        return current_node
        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.tail is None:
            new_node.next = None
            self.tail = new_node
        else:
            self.tail.next = new_node
        
        self.tail = new_node         
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        current = self.tail
        self.tail = current.next
        return current
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        current_head = self.head
        if node is not self.head:
            self.head.prev = node
            self.head = node
            self.head.next = current_head
        else:
            print('this node is already in the head!')

             

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        current_tail = self.tail
        if node is not self.tail:
            self.tail.prev = node
            self.tail = node
            self.tail.next = current_tail
        else:
            print('This node is already in the tail!')    

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        this_node = self.head
        prev_node  = this_node.prev
        while this_node is not None:
            if this_node.value == node:
                if prev_node is not None:
                    prev_node.next = this_node.next
                else:
                    self.head = this_node.next
                return True
            else:
                prev_node = this_node
                this_node = this_node.next
        return False                    

    

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass