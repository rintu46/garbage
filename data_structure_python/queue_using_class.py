



import collections

q = collections.deque()         #deque mean double ended queue, so we can both side append or pop
q.appendleft(10)                # here just try left side append operation
q.appendleft(20)
q.appendleft(30)

print(q)

q.popleft()          # first pop from lest
print(q)

q.pop()               # now pop from right
print(q)



print('-'*100,'\n')



#queue is module but Queue is a class

# queue.Queue(maximus size)    ---> here if the max size is 0 or less than 0 then it will get infinity.. otherwise we can set the size 
# 
# 
# import queue
# q2 = queue.Queue(maxsize=2)
# q2 = queue.Full()
# q2 = queue.Empty()
# print('check',q2)


# put(item, block=True, timeout)    here put this item in the queue and if the block is true and timeout is none, 
# then it will block untill the free slot is availble 
# but if we set the block is false and timeout like 2 then it will give the massage after that time
# also we can use put_nowait(item)



import queue
q3 = queue.Queue()

q3.put(10)
q3.put(50)
q3.put(30)

print(q3)

q3.get()
q3
print(q3)