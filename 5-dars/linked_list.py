class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
        
class LinkedList:
    
    def __init__(self) -> None:
        self.head = Node()
    
    def append(self, data):
        new_data = Node(data)
        current = self.head
        while current.next != None:
            current= current.next
        current.next = new_data
        
    
    def show(self):
        current = self.head

        while current.next !=None:
            current = current.next
            print(current.data)
    


   
    

data = LinkedList()

data.append(5)
data.append("Murodjon")

data.show()