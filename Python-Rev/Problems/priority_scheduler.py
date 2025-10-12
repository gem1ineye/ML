import heapq

# -----------------------------
# Priority Scheduler using heapq (min-heap)
# -----------------------------
class PriorityScheduler:
    def __init__(self):
        # Internal list to store tasks as (priority, task) tuples
        self._task_list = []
    
    # -----------------------------
    # Inner class representing a Task
    # -----------------------------
    class Task:
        def __init__(self, name, priority):
            self.name = name
            self.priority = priority
        
        def __repr__(self):
            # Defines how Task objects are displayed
            return f'name: {self.name}'
    
    # -----------------------------
    # Add a new task with given priority
    # -----------------------------
    def add_task(self, name, priority):
        task = self.Task(name, priority)                   # create Task object
        heapq.heappush(self._task_list, (priority, task))  # push tuple (priority, task) into heap
    
    # -----------------------------
    # Fetch and remove the task with the highest priority (smallest number)
    # -----------------------------
    def next_task(self):
        if self._task_list:
            return heapq.heappop(self._task_list)          # removes and returns smallest priority task
        else:
            return None
    
    # -----------------------------
    # Peek at the next task without removing it
    # -----------------------------
    def peek_task(self):
        if self._task_list:
            return self._task_list[0]                      # just returns top of heap (min element)
        else:
            return None


# -----------------------------
# Object creation and usage
# -----------------------------
sch = PriorityScheduler()

# Adding tasks with priority values (smaller = higher priority)
sch.add_task('update website', priority=2)
sch.add_task('add inventory', priority=1)

# Peeking at the next task (does not remove it)
print(sch.peek_task())   # Output: (1, name: add inventory)
