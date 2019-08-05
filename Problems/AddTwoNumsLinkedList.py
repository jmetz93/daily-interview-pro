# You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    """
    :type l1: Node
    :type l2: Node
    :rtype: Node
    """
    sum = l1.val + l2.val
    carry = int(sum / 10)

    l3 = ListNode(sum%10)
    p1 = l1.next
    p2 = l2.next
    p3 = l3
    while(p1 != None or p2 != None):
        sum = carry + ( p1.val if p1 else 0) + ( p2.val if p2 else 0)
        carry = int(sum/10)
        p3.next = ListNode(sum % 10)
        p3 = p3.next
        p1 = p1.next if p1 else None
        p2 = p2.next if p2 else None
 
    if(carry > 0):
        p3.next = ListNode(carry)
 
    return l3
 

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val,
  result = result.next
# 7 0 8
