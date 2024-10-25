#Leetcode 643: Maximum Average subarray I


# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value
# and return this value.Any answer with a calculation error less than 10-5 will be accepted.
#
# Example 1
# Input: nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75000
# Explanation: Maximum
# average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
# Example 2
# Input: nums = [5], k = 1
# Output: 5.00000

class Solution(object):
    def FixedLengthSubarrayWithMaxAverage( nums, k):
        left=right=sum=0
        #max_avg=-10000
        max_avg=float('-inf')
        fixd_len_cnt=0
        for right in range(len(nums)):
            fixd_len_cnt+=1
            sum=sum+nums[right]
            if fixd_len_cnt>=k:
                #print(sum / fixd_len_cnt)
                max_avg=max(max_avg,sum/fixd_len_cnt)
                sum=sum-nums[left]
                left+=1
                fixd_len_cnt -= 1
        return max_avg

    #print(FixedLengthSubarrayWithMaxAverage([1,12,-5,-6,50,3],4))
    #print(FixedLengthSubarrayWithMaxAverage([5],1))
    print(FixedLengthSubarrayWithMaxAverage([-1], 1))