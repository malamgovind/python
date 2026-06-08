# movie ticket price calculator
# -- movie ticket are priced based on the age : 
# $12 for adults(18 and over), $8 for children. Everone gets a $2 diccount on wednesdays.

age = int(input("Enter your age: "))
days = {
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday",
    "7": "Sunday"
}

print("Select day:")
for key, value in days.items():
    print(key, ":", value)

choice = input("Enter choice (1-7): ")

day = days.get(choice, "Invalid choice")

print("You selected:", day)

price = 12 if age >= 18 else 8 

if day == "Wednesday":
    price -= 2
    print("Today is Wednesday, you get a $2 discount!")

print("your age is: ", age)
print("today is: ", day)
print("your ticket price is: $", price)