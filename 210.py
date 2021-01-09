class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sorting
        # preparation
        vertices = list(range(numCourses))
        out_edge = {n: [] for n in vertices}
        in_degree = {n: 0 for n in vertices}
        for e in prerequisites:
            out_edge[e[1]].append(e[0])
            in_degree[e[0]] += 1
        print(out_edge, '\n', in_degree)

        # topological sorting
        res_list = []
        while any([v == 0 for k, v in in_degree.items()]):
            for k, v in in_degree.items():
                if v == 0:
                    res_list.append(k)
                    del in_degree[k]
                    for i in out_edge[k]:
                        in_degree[i] -= 1
                    break

        if len(in_degree) > 0:
            return []
        else:
            return res_list