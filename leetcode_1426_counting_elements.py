class Solution:
    def countElements(self, arr: List[int]) -> int:
        dict={}
        answer=0
        for i in range(len(arr)):
            if arr[i] in dict:
                dict[arr[i]]+=1
            else:
                dict[arr[i]]=1
        for i in range(len(arr)):
            if arr[i]+1 in dict:
                answer+=1
        return answer