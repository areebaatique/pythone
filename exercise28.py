try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("That is not a valid number.")
