class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        cur_sum=0
        prefix_sum_array=[]
        for i in range(len(nums)):
            cur_sum=cur_sum+nums[i]
            prefix_sum_array.append(cur_sum)

        left_section=right_section=0
        for left in range(len(nums)):
            if left>0:
                left_section=prefix_sum_array[left-1]
            right_section=total-left_section-nums[left]
            if left_section==right_section:
                return left
        return -1