from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dict = defaultdict(int)
        dict[0] = 1
        cnt = answer = 0
        for right in range(len(nums)):
            if not nums[right] % 2 == 0:
                cnt += 1
            if cnt - k in dict:
                answer = answer + dict[cnt - k]
            dict[cnt] += 1
        return answer

