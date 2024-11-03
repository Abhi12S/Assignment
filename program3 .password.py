def checkingForPasswordValidity(password):
    # Minimum length of transaction password: 6
    # Maximum length of transaction password: 12
    
    length = len(password)
    lenghtCondition = ((6 <= length) and (length <= 12))
    # print(lenghtCondition)
    
    if lenghtCondition:
        lowerCount = 0
        upperCount = 0
        digitCount = 0 
        charCount = 0
        for char in password:
            # letter between [a-z]
            if char.islower():
                lowerCount += 1
            if char.isupper():
                upperCount += 1
            if char.isdigit():
                digitCount += 1 
            if char in ("#", "$", "@"):
                charCount += 1 
        if (lowerCount != 0 and upperCount != 0 and charCount != 0 and digitCount != 0):
            print(password)
    



list_of_passwords = ["asqwr1234@1","aF145#","2w3E*","2We3345"]
# print(list_of_passwords)
for i in list_of_passwords:
    input_password = i
    checkingForPasswordValidity(input_password)
