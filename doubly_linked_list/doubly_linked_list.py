"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_next(self):
        return self.next


    def set_next(self, value):
        self.next = value

    def get_prev(self):
        return self.prev   

    def set_prev(self,value):
        self.prev = value   

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev             
            
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
        node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.length +=1
        return self


       
       
       
       
       
       
        # if self.head is None:
        #     new_node = ListNode(value)
        #     self.head = new_node
        #     return
        # new_node = ListNode(value)
        # new_node.next = self.head
        # self.head.set_prev(new_node)
        # self.head = new_node  
        
        
        
        
        
        
        
        
        # new_node  = ListNode(value)
        # self.length += 1 
        # if not self.tail and not self.head:

        #     self.tail = new_node
        #     self.head = new_node

        # else:
        #     self.head.set_prev(new_node)
        #     self.head = new_node
        
               
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # create a reference of the current head value
        # call delete on the self.head
        # return reference
        current_head = self.head.value
        self.delete(self.head)
        return current_head

        
        
        
        
        # current_node  = self.head
        # self.head.set_next(current_node.next)
        # self.head = current_node.get_next()
        # self.head.prev = None
        # return current_node.value
        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length +=1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

            # new_node.next = None
            # self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.set_next(new_node)
            self.tail = new_node
      
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # create a reference of the current tail value
        # call delete on the self.tail
        # return reference

        current_tail = self.tail.value
        self.delete(self.tail)
        return current_tail



        # current = self.tail
        # self.tail.set_next(current.prev)
        # self.tail = current.get_prev
        # self.tail.next = None
        # return current.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if our input equals the head return None
        # store a reference to the inputs value
        # call self.delete on the input
        # self.add_to_head(ode.value)
        if node == self.head:
            return None

        value = node.value
        self.delete(node)
        self.add_to_head(value)


          
       
       
       
       
        # current_head = self.head
        # if node is not current_head:
        #     self.head.set_prev(node)
        #     self.head = node
        #     self.head.set_next(current_head)
        # else:
        #     print('this node is already in the head!')

             

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # check if the input is the tail
        # store a reference of the inputs value
        # call self.delete on the input
        # call add to tail to the reference
        if self.tail == node:
            return None
        value = node.value
        self.delete(node)  
        self.add_to_tail(value) 

        # current_tail = self.tail
        # if node is not current_tail:
        #     self.tail.set_next(node)
        #     self.tail = node
        #     self.tail.set_prev(current_tail)
        # else:
        #     print('This node is already in the tail!')    

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):

        if self.head is None and self.tail is None:
            return None

        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        elif self.head == node:
            self.head = node.next
            node.delete()
        
        elif self.tail == node:
            self.tail = node.prev
            node.delete()

        else:
            node.delete()

        self.length -= 1    
        
        # prev = node.get_prev() #input node's previous pointer
        # next_ = node.get_next() #input node's next pointer

        # # if self.prev:
        # prev.set_next(next_) # setting prev pointer of the input to point towards the inputs next pointer
        # # if self.next:
        # next_.set_prev(prev) # and vice versa
                      

     
        




        # this_node = self.head
        # prev_node  = this_node.prev
        # while this_node is not None:
        #     if this_node.value == node:
        #         if prev_node is not None:
        #             prev_node.next = this_node.next
        #         else:
        #             self.head = this_node.next
        #         return True
        #     else:
        #         prev_node = this_node
        #         this_node = this_node.next
        # return False                    

    

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
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
         
