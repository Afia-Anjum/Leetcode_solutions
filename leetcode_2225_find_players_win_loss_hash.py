from collections import defaultdict
import itertools
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer0=[]
        answer1=[]
        players_list=list(itertools.chain(*matches))
        unique_players=sorted(list(set(players_list)))
        dict=defaultdict(int)
        for key in unique_players:
            dict[key]=0
        for i in range(len(matches)):
            dict[matches[i][1]]+=1
        for key in dict.keys():
            if dict[key]==1:
                answer1.append(key)
            elif dict[key]==0:
                answer0.append(key)
        return [answer0,answer1]
