import collections

DoubleEnded = collections.deque(["Mon", "Tue", "Wed"])

DoubleEnded.append("Thu")

print("Appended at right - ")
print(DoubleEnded)

DoubleEnded.appendleft("Sun")

print("Appended at right at left is - ")
print(DoubleEnded)

DoubleEnded.pop()

print("Deleting from right - ")
print(DoubleEnded)

DoubleEnded.popleft()

print("Deleting from left - ")
print(DoubleEnded)
"""
    A double-ended queue, or deque, supports adding and removing elements from either end. 
    The more commonly used stacks and queues are degenerate forms of deques, 
    where the inputs and outputs are restricted to a single end.
"""