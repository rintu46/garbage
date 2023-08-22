# There are some user defined data structure
# 1. stack
# 2. Queue
# 3. linked list
# 4. tree
# 5. graph


# stack store the item of Last in first out(LIFO) or First in last out(FIFO)
# some basic operation of push, pop, peek or top, isEmpty


# ----------push & pop -------
stack1 = []
print(stack1, type(stack1))
stack1.append(10)
stack1.append(20)
stack1.append(30) #push all the element
print('-'*10,'push all the element', '-'*10,'\n',stack1)
stack1.pop()   #pop the last element only
print('-'*10,'pop the element from top', '-'*10,'\n',stack1)

# here the ordering is LIFO order 

s2 = []
print('we can check the list is empty or not--','\n',len(s2)==0,'\n', 'or we can check also--\n', not(stack1))


# by using indexing method we can access the list element

print('we can check the top element of this list \n',stack1[-1])       



# here we run a very simple program using all operations of stack

print(' here we run a very simple program using all operations of stack \n')


test = []  #define an empty stack

def push():             #push function
    element = input('enter the input number: ')
    test.append(element)
    print(test)

def pop():                             #pop function
    if not test:                       #first we check that the stack is empty or not
        print('the stack is empty')
    else:
        remove = test.pop()
        print('pop the element:', remove)
        print(test)

while True:
    print('please enter the number for - 1.push, 2.pop, 3.quit')
    choich = int(input())                       #take the input from user then call the required function
    if choich==1:
        push()
    elif choich==2:
        pop()
    elif choich==3:                             
        break
    else:
        print('please enter the number 1 for push function and number 2 for pop function')



