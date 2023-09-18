import queue


q = queue.PriorityQueue()          #import the queue as a priority queue
q.put(10)
q.put(60)
q.put(20)
q.put(40)       # input all the value using put  
q.put(40)
 

print(q.get())
print(q.get())
print(q.get())
print(q.get())      # print the values using get function
print(q.get())




# queue like tuple that means priority and value  

q2 = []
q2.append((4, 'four'))
q2.append((2, 'two'))
q2.append((1, 'one'))

q2.append((3, 'three'))



q2.sort(reverse=True)
# q2.sort()
print(q2.pop())
print(q2.pop())
print(q2.pop())
print(q2.pop())