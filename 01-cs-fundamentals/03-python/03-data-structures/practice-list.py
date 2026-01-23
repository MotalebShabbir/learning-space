# List ==================
fruit = ['banana', 'mango', 'barry']
print(fruit)
print(fruit[2])

# add element
fruit.append("grapes")
fruit.insert(2,"tomato")  # insert
print(len(fruit))

#remove element
fruit.remove("banana")      
fruit.pop()                  
fruit.pop(0)                  

# Check existence
print("apple" in fruit)       
print("apple" not in fruit)   

# Sort
fruit.sort()                  
fruit.sort(reverse=True)     