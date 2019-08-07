# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

# Example:
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]

# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]

# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]

class Solution: 
  def getRange(self, arr, target):
    # Fill this in.
    leftSide = 0
    rightSide = len(arr)-1
    foundAt = [-1, -1]
    while leftSide != rightSide:
      if arr[leftSide] == target and foundAt[0] == -1:
        foundAt[0] = leftSide 
      if arr[rightSide] == target and foundAt[1] == -1:
        foundAt[1] = rightSide
      if foundAt[0] == -1:
        leftSide += 1
      if foundAt[1] == -1:
        rightSide -= 1
      if foundAt[0] != -1 and foundAt[1] != -1:
        break
    return foundAt
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

