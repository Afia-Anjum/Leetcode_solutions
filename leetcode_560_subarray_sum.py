from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict=defaultdict(int)
        dict[0]=1
        curr_sum=answer=0
        for i in range(len(nums)):
            curr_sum=curr_sum+nums[i]
            if curr_sum-k in dict:
                answer=answer+dict[curr_sum-k]
            dict[curr_sum]+=1
        return answer