# weather acitivity suggester
# problem : suggest an activity based on the weather conditions.
# -- if the weather is sunny, suggest going for a walk.
# -- if the weather is rainy, sugggest staying indoors and reading a book.
# -- if the weather is snowy, sugegst going skiing or building a snowman.

weather = input("enter the weather condition (sunny, rainy, snowy): ".lower())

if weather == "sunny":
    print("the weather is: ", weather + ", you should go for a walk!")

elif weather == "rainy":
    print("the weather is: ", weather + ", you should stay indoors and read a book!")

elif weather == "snowy":
    print("the weather is : ", weather + ", you should go skiing or build a snowman!")

else:
    print("invalid weather condition, please enter sunny, rainy, or snowy")