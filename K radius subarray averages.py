class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix=[]
        sum=0
        avg_array=[]
        denominator=2*k+1
        for i in range(len(nums)):
            sum=sum+nums[i]
            prefix.append(sum)
        for i in range(len(nums)):
            if i-k < 0 or i+k >= len(nums):
                avg_array.append(-1)
            else:
                avg_array.append((prefix[i + k]-prefix[i-k]+nums[i-k]) // denominator)
        return avg_array