try:
    value = int("Govind")
    print(10 / 0)

except ValueError:
    print("value error")

except ZeroDivisionError:
    print("division error")