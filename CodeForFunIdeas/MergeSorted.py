# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = list1
        print(head.val)
        return list1
    
head = ListNode(0)
head.next = ListNode(1)
for i in range(2,10):
    node = ListNode(i)
    head.next.next = node
    
node = ListNode()
while 








for i in range(0,8,2):
    head = head.next
    
s = Solution()
sortedList = s.mergeTwoLists([1,3,5,7], [2,4,6,8])
print(sortedList)