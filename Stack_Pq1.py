# 1. Reverse a String using a Stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def reverse_string(self, s):
        for char in s:
            self.push(char)
        return ''.join(self.pop() for _ in range(len(s)))

# Example Usage
s = Stack()
print(s.reverse_string("hello"))  # Output: "olleh"


# 2. Stack Sort Algorithm (Using Only Stack Operations)

def sort_stack(stack):
    temp_stack = []
    
    while stack:
        current = stack.pop()
        while temp_stack and temp_stack[-1] > current:
            stack.append(temp_stack.pop())
        temp_stack.append(current)
    
    while temp_stack:
        stack.append(temp_stack.pop())  # Put sorted elements back

    return stack

# Example Usage
stack = [5, 2, 9, 1, 3]
print("Sorted Stack:", sort_stack(stack))  # Output: [1, 2, 3, 5, 9]


# 3. Implement a Stack for Queue Operations (Using Two Stacks)

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

# Example Usage
q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2


# 4. Undo/Redo Operation with Stacks

class UndoRedo:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def perform_action(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear()  # Clear redo when new action is performed

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.undo_stack.pop())

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.redo_stack.pop())

# Example Usage
ur = UndoRedo()
ur.perform_action("Type A")
ur.perform_action("Type B")
ur.undo()
ur.redo()


# 5. Implement a Stack that Supports Getting the Middle Element

class StackWithMiddle:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def get_middle(self):
        if not self.stack:
            return None
        return self.stack[(len(self.stack) - 1) // 2]

# Example Usage
s = StackWithMiddle()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.get_middle())  # Output: 2


# 6. Remove Duplicates from a Stack

def remove_duplicates(stack):
    seen = set()
    new_stack = []
    
    while stack:
        val = stack.pop()
        if val not in seen:
            seen.add(val)
            new_stack.append(val)

    while new_stack:
        stack.append(new_stack.pop())

    return stack

# Example Usage
stack = [1, 2, 3, 2, 4, 1]
print("Unique Stack:", remove_duplicates(stack))  # Output: [1, 2, 3, 4]


# 7. Implement Stack with Two Queues

from collections import deque

class StackWithQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        result = self.q1.popleft() if self.q1 else None
        self.q1, self.q2 = self.q2, self.q1  # Swap queues
        return result

    def peek(self):
        return self.q1[-1] if self.q1 else None

    def is_empty(self):
        return not self.q1

# Example Usage
s = StackWithQueues()
s.push(10)
s.push(20)
print(s.pop())  # Output: 20


# 8. Check if a Stack is Palindrome

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def is_palindrome(self):
        return self.stack == self.stack[::-1]

# Example Usage
s = Stack()
s.stack = [1, 2, 3, 2, 1]
print("Is stack palindrome?", s.is_palindrome())  # Output: True


# 9. Next Greater Element using Stack

def next_greater_element(arr):
    stack, result = [], [-1] * len(arr)
    
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        result[i] = stack[-1] if stack else -1
        stack.append(arr[i])

    return result

# Example Usage
arr = [4, 5, 2, 10, 8]
print("Next Greater Elements:", next_greater_element(arr))  # Output: [5, 10, 10, -1, -1]


# 10. Reverse a Queue using a Stack

from collections import deque

def reverse_queue(q):
    stack = []
    while q:
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
    return q

# Example Usage
q = deque([1, 2, 3, 4, 5])
print("Reversed Queue:", list(reverse_queue(q)))  # Output: [5, 4, 3, 2, 1]


# 11. Remove All Elements Less Than X

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def remove_less_than_x(self, x):
        temp_stack = [val for val in self.stack if val >= x]
        self.stack = temp_stack
        return self.stack

# Example Usage
s = Stack()
s.stack = [3, 10, 1, 7, 2, 12]
print("Modified Stack:", s.remove_less_than_x(5))  # Output: [10, 7, 12]
