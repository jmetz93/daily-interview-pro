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

  for index in range(1,len(nums)):
        value = nums[index]
        i = index-1
        while i>=0:
            if value < nums[i]:
                nums[i+1] = nums[i]
                nums[i] = value
                i -= 1
            else:
                break
  return nums

print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]
