# write your code here
import math
import random

friends = {}
print("Enter the number of friends joining (including you):")
friend_count = int(input())
if friend_count > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(friend_count):
        friend_name = input()
        friends[friend_name] = 0

    # For Inputting bill
    print("Enter the total bill value:")
    bill = int(input())
    split = round((bill/friend_count),2)
    for friend_name in friends:
        friends[friend_name] = split

    # Lucky check
    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    lucky_check = input()

    if lucky_check == "Yes":
        luckey_key = random.choice(list(friends.keys()))
        print(luckey_key, " is the lucky one!")
        
        split = round((bill/(friend_count-1)),2)
        for friend_name in friends:
            if friend_name == luckey_key:
                friends[friend_name] = 0
                continue
            friends[friend_name] = split
    else:
        print("No one is going to be lucky")

    # final output
    print(friends)
else:
    print("No one is joining for the party")
