class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    
    date = None
    next_node = None

    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return "<Node data: %s>" % self.data



class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the linked list
        Take 0(n) time
        """
        
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node


        return count




N1 = Node(10)
print(N1)

N2 = Node(20)
N1.next_node = N2

print(N1.next_node)













