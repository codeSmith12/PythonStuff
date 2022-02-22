# LinkedList.py
class Node:
    def __init__(self, name):
        self.name=name # Data held by the node
        self.next=None # Pointer to the next node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def appendItem(self, data):
        node = Node(data) # Node 2 just created
        if self.tail: # Checks if we have a node already
            self.tail.next = node # Linking the 2 nodes together
            self.tail = node # Move the tail to the end of the list
        else: # If we have an empty list
            self.head = node
            self.tail = node
        self.count += 1
    def printList(self):
        cur = self.head # Get the first node in the list
        while cur: # Run while current is not == to None
            print(cur.name) # Print value of list item
            cur = cur.next # Set cur to next node in list
    def getSize(self):
        return self.count
    def search(self, target): # Target will be string
        cur = self.head # Get the first node in the list
        while cur: # Run while current is not == to None
            if cur.name == target:
                return True
            cur = cur.next # Set cur to next node in list
        return False

ll = LinkedList()
ll.appendItem("Brian")
ll.appendItem("Lekha")
ll.appendItem("Oliver")
ll.appendItem("Jeremy")
ll.printList()
print(ll.search("Lekha"))
