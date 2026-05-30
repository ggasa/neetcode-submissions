# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        ref = head
        while ref:
            arr.append(ref.val)
            ref = ref.next
    
        arr.reverse()
        print(arr)

        print("reverse linked-list....")
        ref2 = head
        i=0

        while i<len(arr):
            ref2.val = arr[i]
            ref2 = ref2.next
            i += 1

        return head