from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        answer = 0
        dict = defaultdict(int)
        str_list = list(text)
        target_str_list = "balloon"
        for i in range(len(str_list)):
            dict[str_list[i]] += 1

        while (True):
            flag = 0
            for i in range(len(target_str_list)):
                if target_str_list[i] in dict.keys() and dict[target_str_list[i]] >= 1:
                    dict[target_str_list[i]] -= 1
                else:
                    flag = 1
                    break
            if flag == 0:
                answer += 1
            if dict[target_str_list[i]] == 0:
                break

        return answer