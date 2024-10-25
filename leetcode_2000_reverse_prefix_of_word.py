class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left=right=0
        word=list(word)
        for i in range(len(word)):
            if word[i] == ch:
                right=i
                break
        while(left<right):
            if word[left]==word[right]:
                right-=1
                left+=1
                continue
            tmp=word[left]
            word[left]=word[right]
            word[right]=tmp
            right-=1
            left+=1
        answer="".join(word)
        return answer