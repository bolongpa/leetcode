class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict_s = {}
        for i in s:
            if i not in dict_s.keys():
                dict_s[i] = 0
            else:
                dict_s[i] += 1

        dict_t = {}
        for i in t:
            if i not in dict_t.keys():
                dict_t[i] = 0
            else:
                dict_t[i] += 1

        for k in dict_t.keys():
            if k not in dict_s.keys():
                return k
            elif dict_t[k] > dict_s[k]:
                return k
