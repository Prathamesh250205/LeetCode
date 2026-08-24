class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        
        next_group = m
        for i in range(n):
            if group[i] == -1:
                group[i] = next_group
                next_group += 1

        item_adj = [[] for _ in range(n)]
        item_indeg = [0] * n
        group_adj = [[] for _ in range(next_group)]
        group_indeg = [0] * next_group

        for i in range(n):
            for u in beforeItems[i]:
                item_adj[u].append(i)
                item_indeg[i] += 1
                if group[u] != group[i]:
                    group_adj[group[u]].append(group[i])
                    group_indeg[group[i]] += 1

        def topo_sort(num_nodes, adj, indeg):
            queue = [node for node in range(num_nodes) if indeg[node] == 0]
            order = []
            indeg = indeg[:] 
            while queue:
                node = queue.pop(0)
                order.append(node)
                for nxt in adj[node]:
                    indeg[nxt] -= 1
                    if indeg[nxt] == 0:
                        queue.append(nxt)
            return order if len(order) == num_nodes else None

        item_order = topo_sort(n, item_adj, item_indeg)
        if item_order is None:
            return []

        group_order = topo_sort(next_group, group_adj, group_indeg)
        if group_order is None:
            return []

        items_by_group = {}
        for item in item_order:
            items_by_group.setdefault(group[item], []).append(item)

        result = []
        for g in group_order:
            result.extend(items_by_group.get(g, []))

        return result