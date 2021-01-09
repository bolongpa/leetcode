class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        while accounts:
            res.append(accounts.pop(0))

            name = res[-1][0]
            queue = res[-1][1:]  # emails to examine
            while queue:
                email = queue.pop(0)
                new_accounts = []
                while accounts:
                    data = accounts.pop(0)
                    if data[0] == name and email in data:
                        queue.extend([i for i in data[1:] if i not in res[-1]])
                        res[-1].extend(data[1:])

                    else:
                        new_accounts.append(data)
                accounts = new_accounts

        for i in range(len(res)):
            processed = sorted(list(set(res[i][1:])))
            res[i] = [res[i][0]] + processed

        return res