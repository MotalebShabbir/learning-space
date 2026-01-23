# Dictonary ==========
user = {'name':'sabbir', 'age':22, 'city':'bogura'}

# Access
print(user)
print(user['name'])
print(user.get('phone','N/A')) # 2nd paramater default value

# add /update
user['phone'] = '017942XXX2424'
user['age'] = 23

# Delate
del user['city']

# check key exists
print('name' in user)

# loop
for v in user:
    print(f"{v} : {user[v]}")

# just key or value
print(user.keys())
print(user.values())