# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a contiguous subarray of which the sum is greater than or equal to s. 
# If there isn't one, return 0 instead.

# Example:

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2

# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

class Solution:
    def minSubArrayLen(self, nums, s):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # ok lwts see
        n=len(nums)
        
        if(n==0):
            return 0
        
        if(s>sum(nums)):
            return 0
        
        m = n
        start = 0
        end = 0
        curr_sum=0
        while(end<n):
                curr_sum+=nums[end]
                while(curr_sum>=s):
                    m=min(end+1-start,m)
                    curr_sum -= nums[start]
                    start+=1
                end+=1
        return m

print Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7)
# 2