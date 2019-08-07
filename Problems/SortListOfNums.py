# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

# Example 1:
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]

# Challenge: Try sorting the list using constant space.

def sortNums(nums):
  # Fill this in.
  # Easy solution:
  # nums.sort()
  # return nums

  n = len(nums)
  for i in range(n):
      for j in range(1,n):
          if nums[j-1] > nums[j]:
              (nums[j-1], nums[j]) = (nums[j], nums[j-1])
  return nums

print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]
