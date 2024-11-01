class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dict={}
        for i in range(0,len(nums)):
            tmp=nums[i]
            for j in range(len(tmp)):
                if tmp[j] in dict:
                    dict[tmp[j]]+=1
                else:
                    dict[tmp[j]]=1
        answer=[]
        for key in dict.keys():
            if dict[key]==len(nums):
                answer.append(key)
        return sorted(answer)
