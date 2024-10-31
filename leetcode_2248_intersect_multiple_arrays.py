from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return (len(set(Counter(s).values()))==1)


# from collections import defaultdict
# class Solution:
#     def areOccurrencesEqual(self, s: str) -> bool:
#         dict=defaultdict(int)
#         for i in range(len(s)):
#             dict[s[i]]+=1
#         return (len(set(dict.values()))==1)


    # def intersection(self, nums: List[List[int]]) -> List[int]:
    #     dict={}
    #     for i in range(0,len(nums)):
    #         tmp=nums[i]
    #         for j in range(len(tmp)):
    #             if tmp[j] in dict:
    #                 dict[tmp[j]]+=1
    #             else:
    #                 dict[tmp[j]]=1
    #     answer=[]
    #     for key in dict.keys():
    #         if dict[key]==len(nums):
    #             answer.append(key)
    #     return sorted(answer)
