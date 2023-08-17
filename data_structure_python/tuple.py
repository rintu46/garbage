# A tuple is created by placing all the items (elements) inside parentheses () , separated by commas. 
# tuples are comma separated elements enclosed within the parentheses


tuple1 = 1,2,3,4
print('-'*10,'make a tuple','-'*10, '\n',tuple1,'\n')

print(type(tuple1))


# ----------- make an empty tuple --------
tuple2 = ()
print('-'*10,'make an empty tuple','-'*10, '\n',tuple2,'\n')
print(type(tuple2))

# ---------- single element tuple -----------

tuple3 = (2)
print('-'*10,'single element tuple','-'*10, '\n', tuple3, type(tuple3),'\n')   # when we just store any single values without commas then it's not a tuple type. it will consider an int type

# ----------- when define a single value with type tuple -----------
tuple4 = (2,)
print('-'*10, 'single value with type tuple', '-'*10, '\n', tuple4, type(tuple4),'\n')



# ----------- tuple is immutable, we can't insert or modify the vaules after creating the tuple ------------
tuple5 = (1,2,3,4)
# tuple5.append(5)


# ----------- nested tuple -------
tuple6 = ((1,2), 1,2,3,4)
print('-'*10, 'nested tuple ', '-'*10, '\n',tuple6,'\n')


# ---------- negative indexing -----------
tuple7 = (1,2,3,4,5)
print('-'*10, 'negative indexing', '-'*10, '\n',tuple7[-2],'\n')




# --------why we need the tuple when we have list ------------
# 1. tuple is faster than list

