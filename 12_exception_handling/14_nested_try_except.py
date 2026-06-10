try:
    try:
        print(1 / 0)
    except ZeroDivisionError:
        print("inner exception!")

except:
    print("outer exception!")