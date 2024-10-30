class Solution:
    def length_longest_substring(s,k):
        dict={}
        left=right=answer=0
        for right in range(len(s)):
            if s[right] in dict:
                dict[s[right]]+=1
            else:
                dict[s[right]] = 1
            while len(dict)>k:
                #if we calculate answer here, make sure to put right index in the correct place
                #answer = max(answer, right-1 - left + 1)
                if dict[s[left]]>1:
                    dict[s[left]]-= 1
                elif dict[s[left]]==1:
                    del dict[s[left]]
                left+=1
            # all computations are done and checked, now usual index minus-ing gives the length of the subarray
            answer = max(answer, right-left+1)
        return answer

    print(length_longest_substring("eceba", 2))

