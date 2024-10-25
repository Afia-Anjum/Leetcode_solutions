class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum_array = [0]
        sum = 0
        for i in range(len(gain)):
            sum = sum + gain[i]
            prefix_sum_array.append(sum)
        return(max(prefix_sum_array))