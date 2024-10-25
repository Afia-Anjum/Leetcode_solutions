
class Solution(object):


    def is_alphabetic(letter):
        if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z'):
            return True
    def reverseOnlyLetters(s):
        left=0
        right=len(s)-1
        while(left<right):
            if not is_alphabetic(s[left]):
                left+=1
                continue
            if not is_alphabetic(s[right]):
                right-=1
                continue
            tmp=s[left]
            s[right]=s[left]
            s[left]=tmp
            left+=1
            right-=1
        return s


    print(reverseOnlyLetters("7_28]"))


##########INSIDE LEETCODE SOLUTION SUBMITTED BY ME#########
# class Solution:
#
#     def is_alphabetic(self, letter : chr) -> bool:
#         if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z'):
#             return True
#
#     def reverseOnlyLetters(self, s: str) -> str:
#         left=0
#         right=len(s)-1
#         s=list(s)
#         answer=[]
#         while(left<right):
#             if not self.is_alphabetic(s[left]):
#                 left+=1
#                 continue
#             if not self.is_alphabetic(s[right]):
#                 right-=1
#                 continue
#             tmp=s[left]
#             s[left]=s[right]
#             s[right]=tmp
#             left+=1
#             right-=1
#         return("".join(s))