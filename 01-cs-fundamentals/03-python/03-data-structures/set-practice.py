# set ============
username = {"sabbir", "rahim", "rakib", "shawon"}

# add/remove
username.add('rabbir')
username.remove('rakib')

# check
print('sabbir' in username)

# set operation
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print (a & b) # intersection
print (a | b) # union
print (a - b) # substrction