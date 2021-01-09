class Solution:
    def numDecodings(self, s: str) -> int:
        dic = {len(s):1}
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dic[i] = 0
            else:  # s[i] is not 0
                if i == len(s)-1:
                    dic[i] = 1
                else:  # i < len(s)
                    if int(s[i:i+2]) <= 26:
                        dic[i] = dic[i+1] + dic[i+2]
                    else:
                        dic[i] = dic[i+1]
        print(dic)
        return dic[0]