####This is a O(n) solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=right=0
        answer=inf
        cur_sum=0
        length=0
        flag=0
        for right in range(len(nums)):
            cur_sum=cur_sum+nums[right]
            while cur_sum>=target:
                flag=1
                length=right-left+1
                answer=min(answer,length)
                cur_sum=cur_sum-nums[left]
                left+=1
        if flag==0:
            return 0
        return answer


#Prefix sum solution
        # prefix_array=[]
        # cur_sum=0
        # for i in range(len(nums)):
        #     cur_sum=cur_sum+nums[i]
        #     prefix_array.append(cur_sum)
        # print(prefix_array)
##########O(nlogn) soln would be??:

