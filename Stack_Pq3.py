# 1. Convert Postfix to Infix

def postfix_to_infix(expression):
    stack = []
    
    for char in expression.split():
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(f"({op1} {char} {op2})")
    
    return stack[0]

# Example Usage
postfix_expr = "a b + c d e + * -"
print("Infix Expression:", postfix_to_infix(postfix_expr))  
# Output: "((a + b) - (c * (d + e)))"


# 2. Convert Postfix to Prefix

def postfix_to_prefix(expression):
    stack = []
    
    for char in expression.split():
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(f"{char} {op1} {op2}")
    
    return stack[0]

# Example Usage
postfix_expr = "A B + C D - *"
print("Prefix Expression:", postfix_to_prefix(postfix_expr))
# Output: "* + A B - C D"


# 3. Convert Prefix to Postfix

def prefix_to_postfix(expression):
    stack = []
    
    for char in reversed(expression.split()):
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"{op1} {op2} {char}")
    
    return stack[0]

# Example Usage
prefix_expr = "* + A B - C D"
print("Postfix Expression:", prefix_to_postfix(prefix_expr))
# Output: "A B + C D - *"


# 4. Implement Multiple Stacks using a Single List

class MultiStack:
    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.array = [None] * (num_stacks * stack_size)
        self.tops = [-1] * num_stacks  # Store top index of each stack

    def push(self, stack_num, value):
        if self.tops[stack_num] + 1 < self.stack_size:
            self.tops[stack_num] += 1
            self.array[stack_num * self.stack_size + self.tops[stack_num]] = value
        else:
            print(f"Stack {stack_num} is full!")

    def pop(self, stack_num):
        if self.tops[stack_num] >= 0:
            index = stack_num * self.stack_size + self.tops[stack_num]
            value = self.array[index]
            self.array[index] = None
            self.tops[stack_num] -= 1
            return value
        else:
            print(f"Stack {stack_num} is empty!")
            return None

    def peek(self, stack_num):
        if self.tops[stack_num] >= 0:
            return self.array[stack_num * self.stack_size + self.tops[stack_num]]
        else:
            return None

# Example Usage
stacks = MultiStack(3, 5)  # 3 stacks, each of size 5
stacks.push(0, 10)
stacks.push(1, 20)
stacks.push(2, 30)

print(stacks.pop(1))  # Output: 20
print(stacks.peek(0))  # Output: 10
