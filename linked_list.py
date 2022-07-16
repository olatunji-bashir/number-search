from ast import Return
from turtle import position


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

    def add(self, data):
        """
        Adds a new Node containing data at head of the list
        Takes 0(1) time
        """
        
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        return the node or 'None' id not found

        Takes 0(n) time
        """
        
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertion tkes 0(1) time but finding the node at the 
        insertion point takes 0(n) time.

        Takes overall 0(n) time
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = Node.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None if the key doesn't exist
        Takes 0(n) time 
        """
        
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        
        return current



    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        
        return  '-> '.join(nodes)



N1 = Node(10)
print(N1)

N2 = Node(20)
N1.next_node = N2

print(N1.next_node)


l = LinkedList()
N1 = Node(10)
l.head = N1
print(l.size())


l = LinkedList()
l.add(1)
print(l.size())

l.add(2)
l.add(3)
print(l.size())

print(l)

print(l.search(1))

































