class Numbers:

    def __contains__(self, item):
        return item in [10, 20, 30]

numbers = Numbers()

print(20 in numbers)

# 20 in numbers
# ↓
# numbers.__contains__(20)
# ↓
# True