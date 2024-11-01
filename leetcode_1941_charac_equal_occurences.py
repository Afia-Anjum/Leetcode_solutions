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
