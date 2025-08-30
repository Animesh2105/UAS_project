ls = [1,2,3,'a','b']
ls.append('c')      #adds element to the end of the list
ls.extend(['d','e', 4]) #adds multiple elements to the end of the list
ls.insert(5, 'apple')  #adds apple at index 5
print(f"{ls}")
ls.remove('apple')  #removes first occurence of apple
ls.pop(2)       #removes item at index 2
print(f"{ls}")
for i in ls:
    print(i)
#tuples(created with () instead of [], are similar to lists but are immutable)


di = {"name": "animesh", "age": 19, "nationality": "indian"} #a dictionary holds the data in a key:value type of pairing
print(di["name"])
for keys in di:
    print(keys)     #this lets us iterate over the keys
for value in di.values():
    print(value)    #this lets us iterate over the values
for key, value in di.items():
    print(f"{key}: {value}")    #this lets us iterate over key-value pairs
d = {"name": "animesh", "age": 19, "marks": {"physics": 20, "maths": 19, "chemistry": 18}}  #this is a nested dictionary
print(d["marks"]["physics"])    #accessing value in a nested dictionary

