def print_numbers():
    for spam in range(1, 101):

        if spam % 5 == 0 and spam % 7 == 0:
            print("ChickenMonkey")
            continue
        if spam % 5 == 0:
            print("Chicken")
        elif spam % 7 == 0:
            print("Monkey")
        else:
            print(spam)

print_numbers()