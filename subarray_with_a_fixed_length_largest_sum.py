# Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the
# largest sum whose length is k.


class Solution(object):
    def FixedLengthSubarrayWithLargestSum( nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=right=largest_sum=answer=0
        fixd_length_curr=0

        for right in range(len(nums)):
            largest_sum=largest_sum+nums[right]
            fixd_length_curr+=1
            while fixd_length_curr>=k:
                answer = max(answer, largest_sum)
                print(answer)
                print(fixd_length_curr)
                largest_sum=largest_sum-nums[left]
                fixd_length_curr -= 1
                left += 1
        return answer

    print(FixedLengthSubarrayWithLargestSum([3,-1,4,12,-8,5,6],4))
#
######leetcodesolution#########
# class Solution(object):
#     def find_best_subarray(nums, k):
#         curr = 0
#         for i in range(k):
#             curr += nums[i]
#
#         ans = curr
#         for i in range(k, len(nums)):
#             curr += nums[i] - nums[i - k]
#             ans = max(ans, curr)
#         return ans
#
#     print(find_best_subarray([3,-1,4,12,-8,5,6],4))