class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        new_tasks = defaultdict(list)
        for i, t in enumerate(tasks):
            new_tasks[t[0]].append([t[1], i])
        taskOrder = sorted(new_tasks.keys(), reverse=True)

        heap = new_tasks[taskOrder[-1]]
        heapq.heapify(heap)
        res = []
        currTime = taskOrder[-1]
        taskOrder.pop()
        while heap:
            time, index = heapq.heappop(heap)
            res.append(index)
            currTime = currTime + time
            if not heap and taskOrder and currTime < taskOrder[-1]:
                currTime = taskOrder[-1]
            while taskOrder and currTime >= taskOrder[-1]:
                for t in new_tasks[taskOrder[-1]]:
                    heapq.heappush(heap, t)
                taskOrder.pop()
        return res