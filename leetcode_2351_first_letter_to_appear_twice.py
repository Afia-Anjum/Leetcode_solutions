class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dict={}
        s=list(s)
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]]=dict[s[i]]+1
                return s[i]
            else:
                dict[s[i]]=1