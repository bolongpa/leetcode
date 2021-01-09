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

'''
# Official solution
from collections import defaultdict, deque
class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []
'''