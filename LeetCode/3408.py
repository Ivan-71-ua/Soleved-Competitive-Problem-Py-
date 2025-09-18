import heapq
from typing import List


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.queue_task = []
        self.task_info = {}
        for user_id, task_id, priority in tasks:
            self.task_info[task_id] = (priority, user_id)
            heapq.heappush(self.queue_task, (-priority, -task_id))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = (priority, userId)
        heapq.heappush(self.queue_task, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        _, user_id = self.task_info[taskId]
        self.task_info[taskId] = (newPriority, user_id)
        heapq.heappush(self.queue_task, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.task_info[taskId]

    def execTop(self) -> int:
        heap = self.queue_task
        while heap:
            neg_priority, neg_task_id = heapq.heappop(heap)
            cur_priority, user_id = -1, -1
            if -neg_task_id in self.task_info:
                cur_priority, user_id = self.task_info[-neg_task_id]
            if cur_priority == -neg_priority:
                del self.task_info[-neg_task_id]
                return user_id

            if cur_priority > 0:
                heapq.heappush(heap, (-cur_priority, neg_task_id))
        return -1




# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()