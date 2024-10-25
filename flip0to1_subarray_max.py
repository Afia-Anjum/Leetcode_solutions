### Max Consecutive Ones III

#Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example# 1:
#
# Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
# Output: 6
# Explanation: [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]

# Example 2:
#
# Input: nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k = 3
# Output: 10
# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

class Solution:
    def longestOnes(nums, k):
        left=length=answer=0
        for right in range(len(nums)):
            if nums[right]==0:
                length+=1
            while length>k:
                if nums[left]==0:
                    length-=1
                left+=1
            answer = max(answer, right - left + 1)
        return answer

    print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],2))
    print(longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))