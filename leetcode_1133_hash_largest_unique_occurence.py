from collections import defaultdict


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        answer = []
        for i in range(len(nums)):
            dict[nums[i]] += 1

        for key in dict.keys():
            if dict[key] == 1:
                answer.append(key)

        if len(answer) == 0:
            return -1
        else:
            return max(answer)
