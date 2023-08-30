import collections 

# create a stack
stack = collections.deque()
print("empty stack:  ",stack)

stack.append(10)
stack.append(20)

print("after adding the values:  ",stack)

# stack.pop()
print("pop out the element:  ",stack)

check = not stack
print("check wheather the stack is empty or not: ", check, "\ncheck the number of element has in the stack: ",len(stack), "\nprint the top element of stack: ", stack[-1])