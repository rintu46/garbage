# set is a collection of unique elements, so that in set no item can be repeated
# to create a empty set we need to declear a empty set constructor


# create an empty set
s = set()
print('-'*10, 'create an empty set', '-'*10, '\n', s, 'set-type:',type(s),'\n')

s1 = set('good afternoon')  # the repeated elements are ignored
print(s1)
s2 = set([1,2,3,4])
print(s2)
s3 = {2,1,3,4}
print(s3, '\n')

# set is also an unorder 
r = s2==s3
print(r)


# set is mutable
s2.add(5)
print('-'*10, 'set is mutable', '-'*10, '\n', s2, '\n')


# ** set cannot be nested


# we can check the set elements using loop
s5 = {1,'good afternoon', 2.3}
print('-'*10, 'print the set elements', '-'*10, '\n',s5)
check = 1 in s5
print('-'*10, 'lets check the given elements exist or not', '-'*10, '\n',check)

for i in s5:
    print('-'*10, 'print the set elements using for loop', '-'*10, '\n',i)