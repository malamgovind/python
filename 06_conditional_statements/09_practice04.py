# Fruit ripeness checker
# problem : determind if a fruit is ripe, unripe, or overripe based on its color. 
# -- if the color is green, the fruit is unripe. 
# -- if the color is yellow, the fruit is ripe. 
# -- if the color is brown, the fruit is overripe.

fruit = input("enter the fruit name: ".lower())
color = input("enter the color of the fruit: ".lower())

if color == "green":
    print("the color is fruit is: ", color + " is unripe")

elif color == "yellow":
    print("the color is fruit is: ", color + " is ripe")

elif color == "brown":
    print("the color is fruit is: ", color + " is overripe")

else:
    print("invalid color, please enter green, yellow, or brown")