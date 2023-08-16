# ----------- how to create a list ---------

list1 =  [1,2,3,4]      #we can define a list like this 
list2 = list()    # also we can define a list as a constructor

print(list1, list2)


# --------- how to store data inside list --------
list3 = [1, "one", 1.2, "hello"]  #we can store various type of data inside list

print(list3)



# ----------- list are ordered ---------
list4 = [1,2,3,4,5]   # list is called 0 indexing
print(list4[0], list4[3])

print(list4[-1], list4[-4])   # it also allow neg indexing



# ---------- list can be nested ---------
list5 = [[1,2], 1,2,3,4]  # here we can store another list inside the list
print(list5)

# -------- list are mutable -----------
list6 = [1,2,3,4]
list6.append(6)  #we can modify the list
print(list6)


del list6[2]  #delete any value 
print(list6)




# ---------- list are dynamic -----------
# we can detele or add any value of list so that it can called list are dynamic

