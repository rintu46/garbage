str1 = 'Good Morning'
var2 = list(str1)
var2[12:] = list(' python')

print("".join(var2))



# -------- this one from source
str2 = 'Programming'
var3 = list(str2)
var3[1:6] = list('Python') 

# print(type(var3))
print("".join(var3))