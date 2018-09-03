def validate1(areaCode):
    while areaCode < 100 or areaCode > 999:
        areaCode = int(input("The area code you have entered is invalid, please re-enter your 3 digit area code: "))

def validate2(phoneNumber):
    while phoneNumber< 1000000 or phoneNumber > 9999999:
        phoneNumber = int(input("Phone number invalid, please re-enter: "))

cont = "y"

while cont == "y":

    areaCode = int(input("Please enter your area code: "))
    validate1(areaCode)
    phoneNumber = int(input("Please enter your phone number: "))
    validate2(phoneNumber)
    sentMessages = int(input("Please enter the number of text messages: "))
    beforeTax = int()
    afterTax = int()
    localTax = 1.12
    bill = 5


#when the number of messages is less than 60
    if sentMessages <= 60:
        beforeTax = bill
        afterTax = beforeTax * localTax

#When the number of messages is greater than 60 but less than 180
    elif sentMessages > 60 and sentMessages <= 180:
        beforeTax = bill + (sentMessages - 60) * 0.05
        afterTax = beforeTax * localTax

#When the number of messages if greater than 180
    else:
        beforeTax = bill + (120 * 0.05) + (sentMessages - 180) * 0.10
        afterTax = beforeTax * localTax

    print("Phone number: " + str(phoneNumber))
    print("Area code: " + str(areaCode))
    print("Number of texts: " + str(sentMessages))
    print("Before tax bill: " + str(beforeTax))
    print("After tax bill: %.2f" % afterTax)
    cont = input("Continue?(y/n): ")