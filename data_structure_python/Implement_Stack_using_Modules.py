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





# --------------------- queue ---------------
import queue
stack2 = queue.LifoQueue()
print("LIFO queue type: ",type(stack2))


# insert the data using put function
stack2.put(11)
stack2.put(12)
stack2.put(13)

#show the queue elements using stack2.get()

print('print the number: ',stack2.get(),stack2.get(),stack2.get())
print("\n",stack2.get(timeout=1))

# when the queue get empty we need to set the timeout to stop the queue otherwise
# it will take more time to stop



# in this section we try to cover the basics of collections and queue module 