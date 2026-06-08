# age Group Categories
# -- Classify a person's age group : children(<13), teenager(13-18), adult(18-60), senior(>60)

age = int(input("Enter your age: "))

if age < 13:
    print("your are a child: ", age)
elif age >= 13 and age <= 18:
    print("you are a teenager: ", age)
elif age > 18 and age <= 60:
    print("you are an adult: ", age)
else:
    print("you are a senior: ", age)