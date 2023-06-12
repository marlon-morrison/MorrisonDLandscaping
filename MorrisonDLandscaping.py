print(
"""
            Welcome to Dave Landscaping!
            
Prices for dirt "normal" $10, "rocky" $13, "roots" $18
"""
)

soilType = (["normal", 10], ["rocky", 13], ["roots", 18])
soil = ""
price = 0
cube = 0

length = int(input("\nEnter the length of the hole in feet and next will be inches: "))
length2 = int(input("\nIf you have inches left over enter it here(if not enter 0): "))

width = int(input("\nEnter the width of the hole in feet and next will be inches: "))
width2 = int(input("\nIf you have inches left over enter it here(if not enter 0): "))

depth = int(input("\nEnter the depth of the hole in feet and next will be inches: "))
depth2 = int(input("\nIf you have inches left over enter it here(if not enter 0): "))

answer = input("\nEnter one of the three soil types normal, rocky, or roots ")
if answer == "normal":
   soil = soilType[0][0]
   price = soilType[0][1]
elif answer == "rocky":
   soil = soilType[1][0]
   price = soilType[1][1]
else:
   soil = soilType[2][0]
   price = soilType[2][1]

length = length + (length2 * 0.0833)
width = width + (width2 * 0.0833)
depth = depth + (depth2 * 0.0833)
cube = length * width * depth

price = price * cube

print("Your total price is:$", "{:.2f}".format(price), "\nYou ask for", answer,"soil and the size of the hole is", "{:.2f}".format(cube), "cubic feet. \nSo with that your price is $", "{:.2f}".format(price))

input("\n\nPress the enter key to exit.")