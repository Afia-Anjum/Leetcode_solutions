class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left=right=max_length=answer=0
        cur_sum=0
        for right in range(len(s)):
            cur_sum=cur_sum+ abs(ord(s[right])-ord(t[right]))
            max_length=right-left+1
            if cur_sum>maxCost:
                max_length=max_length-1
                answer=max(answer,max_length)
                cur_sum=cur_sum-(abs(ord(s[left])-ord(t[left])))
                left+=1
        return max(max_length,answer)
