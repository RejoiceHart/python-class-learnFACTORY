colours = ["red", "orange", "yellow", "green", "red"]
print(colours)
print(type(colours))
print(colours[1 : 3])
print(colours.index("red"))
colours.append("Pink")
print(colours)
colours.clear()
print(colours)
colours.copy()
print(colours)

colours = ["red", "orange", "yellow", "green",]
# colours.count()
# print(colours)

print(colours[0])
colours[0] =  "black"
print(colours)
print("Original list contents:", colours)

colours[1] = colours[3]  
# Copying value of the fifth element to the second.
print("Previous list contents:", colours) 

print("\nList length:", len(colours))

colours = ["red", "orange", "yellow", "green"]
newlist = [x for x in colours if "r" in x ]
print(newlist)

colours = ["red", "orange", "yellow", "green"]
colours.pop()
print(colours)

colors = list(("red", "orange", "Yellow"))
print(colors)
print(type(colors))
print(colors[2: ])
colors[1] = "Green"
print(colors)
colors[2 : ] = ["Pink", "Blue", "Ash", "Grey"]
print(colors)
print(len(colors))
colors.insert(1, "purple")
print(colors)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
tropical.extend(thislist)
print(tropical)
print('************')
thislist.remove("cherry")
print(thislist)
print('************')
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print('************')
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print('************')
thislist = ["apple", "banana", "cherry"]
del thislist    
print('************')
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print('************')

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
print('************')
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
      
if x == "banana":
    break  
print('************')
for b  in "Martha":
    print(b) 
# lst = [1, 2, 3, 4]
# lst[0] # 1
# lst[1] # 2    
        

