# dictionary_name = {key1:value1, key2:value2, .........}   here key is immutable and unique

# create empty dictionary


d = {}
print('-'*10, 'create empty dictionary', '-'*10, '\n' ,d, '\n', type(d), '\n')


d1 = {'person1':'p1@gmail.com', 'person2':'p2@gmail.com'}
print('-'*10, 'dictionary example','-'*10, '\n', d1, '\n')


# create a constructor with empty dict
d2 = dict()
print('-'*10, 'create a constructor with empty dict','-'*10, '\n', d2,'\n', type(d2), '\n')


# in dictionary keys are unique, so that we can't dublicate any keys
d3 = {'person1':'gmail: p1@gmail.com', 'person2':'gmail: p2@gmail.com','person1':'gmail:p3@gmail.com'}
print('-'*10, 'we can not dublicate any keys','-'*10, '\n',d3, '\n')  #here the dublicate key is not work


# dictionary is unordered, if we need to short it then we have to do shorting manually
r = d1==d2
print(r)


# access the dictionary values
d4 = {'person1': 'p1@gmail.com', 'person2':'p2@gmail.com'}
print('-'*10, 'access the dictionary values','-'*10,'\n', d4['person1'], '\n')     #we can access the value using the key

del d4['person1']
print('-'*10, 'detele the dictionary key values','-'*10,'\n', d4 , '\n')


d4['person4'] = 'p4@gmail.com'   #dictionary is a mutalbe so that we can add any values using the key 
print('-'*10, 'add the values in dictionary','-'*10,'\n', d4 , '\n')


# --------- we can use values one dictionary to another dictionary but we can't use keys -------------------
