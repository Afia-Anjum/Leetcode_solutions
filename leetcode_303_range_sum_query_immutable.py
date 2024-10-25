class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum_array = []
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            self.prefix_sum_array.append(sum)
        #print(self.prefix_sum_array)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            tmp = self.prefix_sum_array[right] - self.prefix_sum_array[left - 1]
        else:
            tmp = self.prefix_sum_array[right]
        return tmp

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)