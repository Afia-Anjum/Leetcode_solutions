#to get all possible subarrays within a fixed length: right-left+1

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<=1:
            return 0
        left=right=answer=0
        prod=1

        for right in range(len(nums)):
            prod=prod*nums[right]
            print(prod)
            #answer+=1
            while prod>=k:
                prod //= nums[left]
                left+=1
                #answer-=1
            answer=answer+right-left+1
        return answer