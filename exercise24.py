def write_friends(filename, friends_list):
    with open(filename, 'w') as f:
        for friend in friends_list:
            f.write(friend + "\n")

# Example:
friends = ["Sara", "Ahmed", "Maya", "John"]
write_friends("friends.txt", friends)

