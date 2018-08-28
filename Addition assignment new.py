numbersToBeAdded = int(input("How many numbers do you want to add? "))
arr = []
for num in range(0, numbersToBeAdded):
    arr.append(int(input("Enter the next number: ")))
print("the total sum is " + str(sum(arr)))
