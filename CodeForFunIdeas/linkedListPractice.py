
class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next
    
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.list = None
    

    def getSize(self):
        point = self.head
        count=0
        while point is not None:
            point = point.next
            count+=1
        print(count)

        
    # How to accomplish this:
    '''
        Iterate through list 1, only moving on once a node has been added to the merged list
        check if current list1 node is less than cur list2 node
        Add which ever is lower on the list, and move the cur node up the linked list.
    '''
    def mergeTwoLists(self, list1, list2):
        while list1 is not None and list2 is not None:
            if self.list is None:
                if list1.val < list2.val:
                    print("first")
                    self.list = Node(list1.val, None)
                    list1 = list1.next
                    self.head = self.list
                elif list1.val > list2.val:
                    print("second")
                    self.list = Node(list2.val, None)
                    list2 = list2.next
                    self.head = self.list
                else:
                    self.list = Node(list1.val, None)
                    list1 = list1.next
                    self.head = self.list
            else:
                if list1.val < list2.val:
                    self.list.next = Node(list1.val, None)
                    list1 = list1.next
                elif list1.val > list2.val:
                    self.list.next = Node(list2.val, None)
                    list2 = list2.next
                else:
                    self.list = Node(list1.val, None)
                    list1 = list1.next
                self.list = self.list.next

        # Add the remaining items of the list if they are different sized
        while list1 is not None:
            self.list = Node(list1.val)
            list1 = list1.next
        while list2 is not None:
            self.list = Node(list2.val)
            list2 = list2.next
        return LinkedList(self.head)



                
        
    
    def traverse(self):
        point = self.head
        while point is not None:
            print(point.val)
            point = point.next


# Construct odds list
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(4)


list2 = Node(1)
list2.next = Node(3)
list2.next.next = Node(4)
cur = list2
# while cur is not None:
#     print(cur.val)
#     cur = cur.next
# prev = list1
# for i in range(3,93,2):
#     node = Node(i)
#     prev.next = node
#     prev=node

# Construct evens list
list0 = Node(0)
# prev = list0
# for i in range(2,100,2):
#     node = Node(i)
#     prev.next = node
#     prev=node

ll = LinkedList()
test = ll.mergeTwoLists(list1, list2)
test.traverse()
# test.getSize()


