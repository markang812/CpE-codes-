total = int(input("Enter a number: "))
question = input("Do you want to add a number?(yes or no) ").lower()
while question == "yes":
        toBeAdded = input("Enter a number to be added: ")
        total += int(toBeAdded)
        print("the sum is " + str(total))
        question = input("Do you want to add a number?(yes or no) ").lower()


print("the final sum is " + str(total))
