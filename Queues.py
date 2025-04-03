# 1. Queue using Two Stacks (Array or List-based)
# We implement a queue using two stacks:

# Stack 1 is used for enqueue operations.

# Stack 2 is used for dequeuing elements.

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # Transfer stack1 to stack2
        return self.stack2.pop() if self.stack2 else None

    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        elif self.stack1:
            return self.stack1[0]
        return None  # Queue is empty

    def is_empty(self):
        return not self.stack1 and not self.stack2

# Example Usage
q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2


# 2. Reverse a Queue Using Recursion
# This function reverses a queue using recursion.

from collections import deque

def reverse_queue(q):
    if not q:
        return
    front = q.popleft()  # Dequeue front element
    reverse_queue(q)
    q.append(front)  # Enqueue at the end

# Example Usage
queue = deque([1, 2, 3, 4, 5])
reverse_queue(queue)
print(list(queue))  # Output: [5, 4, 3, 2, 1]


# 3. Design a Queue that Supports max() Operation

from collections import deque

class MaxQueue:
    def __init__(self):
        self.queue = deque()
        self.max_deque = deque()  # Stores max elements

    def enqueue(self, x):
        self.queue.append(x)
        while self.max_deque and self.max_deque[-1] < x:
            self.max_deque.pop()  # Remove smaller elements
        self.max_deque.append(x)

    def dequeue(self):
        if self.queue:
            if self.queue[0] == self.max_deque[0]:
                self.max_deque.popleft()  # Remove max if it's dequeued
            return self.queue.popleft()
        return None

    def max(self):
        return self.max_deque[0] if self.max_deque else None

# Example Usage
mq = MaxQueue()
mq.enqueue(3)
mq.enqueue(1)
mq.enqueue(5)
print(mq.max())  # Output: 5
mq.dequeue()
print(mq.max())  # Output: 5


# 4. Merge Two Queues

from collections import deque

def merge_queues(q1, q2):
    merged_queue = deque()
    
    while q1 or q2:
        if q1:
            merged_queue.append(q1.popleft())
        if q2:
            merged_queue.append(q2.popleft())

    return list(merged_queue)

# Example Usage
q1 = deque([1, 3, 5])
q2 = deque([2, 4, 6])
print(merge_queues(q1, q2))  # Output: [1, 2, 3, 4, 5, 6]


# 5. Queue with Count of Specific Element

from collections import deque

def count_element(q, x):
    return q.count(x)

# Example Usage
queue = deque([1, 2, 3, 2, 2])
print(count_element(queue, 2))  # Output: 3


# 6. Reverse Words in a Sentence Using Queue

from collections import deque

def reverse_sentence(sentence):
    words = deque(sentence.split())
    reversed_words = deque()
    
    while words:
        reversed_words.appendleft(words.popleft())  # Reverse using queue

    return " ".join(reversed_words)

# Example Usage
print(reverse_sentence("Hello World"))  # Output: "World Hello"


# 7. Queue that Supports contains(x) Operation

from collections import deque

class QueueWithContains:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None

    def contains(self, x):
        return x in self.queue  # O(n) search

# Example Usage
q = QueueWithContains()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.contains(20))  # Output: True
print(q.contains(40))  # Output: False
