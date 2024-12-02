class Node():
    def __init__(self, value, next=None): 
        self.value = value
        self.next = next

class Linked():
    def __init__(self):
        self.head = None
        v1 = Node(1)
        v2 = Node(2)
        v3 = Node(3)
        
        self.head = v1
        v1.next = v2
        v2.next = v3
    
    def insert_at_begin(self):
        v4 = Node(4)
        v4.next = self.head
        self.head = v4
    
    def insert_at_end(self):
        v5 = Node(5)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = v5
    
    def delete_at_begin(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
    
    def delete_at_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            
ll = Linked()
ll.insert_at_begin()
ll.insert_at_end()
ll.display()
print("Deletion")
ll.delete_at_begin()
ll.delete_at_end()
ll.display()
    