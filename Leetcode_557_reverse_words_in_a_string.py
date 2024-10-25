class Solution(object):
    def reverseWords(s):
        s=s.split()

        answer=[]

        for i in range(len(s)):
            left=0
            right=len(s[i])-1
            string1=s[i]
            string1=list(string1)
            while left<right:
                if not left==right:
                    tmp=string1[left]
                    string1[left]=string1[right]
                    string1[right]=tmp
                    left+=1
                    right-=1
            answer.append("".join(string1))
        return(" ".join(answer))

    print(reverseWords("Let's take LeetCode contest"))