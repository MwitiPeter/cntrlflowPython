#using while loop

whcolors =["blue","yellow","black","white","brown"]
mywhcolors = "brown"

length = len(whcolors)
count = 0

while count < length:
    print(whcolors[count])

    if whcolors[count]== mywhcolors:
        print("This ids the color i want")
        break
    count +=1

    
