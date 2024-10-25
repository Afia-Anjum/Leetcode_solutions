class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dict={}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]]=dict[s[i]]+1
                return s[i]
            else:
                dict[s[i]]=1

####with a set
# class Solution:
#     def repeatedCharacter(self, s: str) -> str:
#         seen=set()
#         for i in range(len(s)):
#             if s[i] in seen:
#                 return s[i]
#             else:
#                 seen.add(s[i])
