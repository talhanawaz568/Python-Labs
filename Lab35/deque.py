from collections import deque
d = deque()
d.append('task1')
d.append('task2')
last_task = d.pop()
print("Popped from the right:", last_task)
d.appendleft('task0')

first_task = d.popleft()
print("Popped from the left:", first_task)
