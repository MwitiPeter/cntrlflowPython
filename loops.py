#for loops
names = ["paul","Mwiti","Jeff"]
for name in names:
    print (name)
   

#for loops using values
My_loop = "Hey world"

for i in range(5):
    print(My_loop)

#while loop as long as the condition is true
count = 0
while count <= 2:
    print (count)
    count += 1

# add a loop then break
colors = ["blue","greean","black"]
mycolor= "yellow"

for color in colors:
    if color == mycolor:
        print("My color is there")
        break
    else:
        print("Not found!")

