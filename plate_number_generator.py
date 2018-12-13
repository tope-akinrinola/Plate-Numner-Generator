import string
import random
# User inputs a username
username = input("Enter you username: ")  
# user inputs a password
password = input("Please input our password: ")

print("You are logged in", username)

print("Here are a list of Local governments to select from")
# Accepted LGI codes
print("ALI, MUS, IKR, ETI")
lgis = ["ALI", "MUS", "IKR", "ETI", "AGE"]

# User enters an LGI
lgi = input("Enter an LGI: ")

# Execute if inputed LGI is in list
if lgi in lgis:   
    last_generated_number = random.randint(1, 999)
    last_char = random.choice(string.ascii_uppercase)
    second_to_last_char = random.choice(string.ascii_uppercase)

    plates = []
    amount = int(input("How many plates do you want to generate: "))
    x= 1
    # if x is not equal to number to be generated
    while x <= amount:
        new_num = last_generated_number + x

        if new_num < 1000:

            if new_num in range(1,9):
                plate = lgi + "00" + str(new_num) + second_to_last_char + last_char
            elif new_num in range(10, 99):
                plate = lgi + "0" + str(new_num) + second_to_last_char + last_char
            else:
               plate = lgi + str(new_num) + second_to_last_char + last_char 

            plates.append(plate)
            print("New plate generated: ", plate)
            # increment x
            x = x + 1
        else:
            # ord() is to get the ASCII number. Adding one if plate number is more than 1000
            # chr convers ascii number back to charcater 
            plate = lgi + str(new_num + 1) + second_to_last_char + chr(ord(last_char) + 1)
            # convert the plate number to a list and remove the first 1 in the string
            pList = list(plate)
            pList[3] = ""
            # convert the list back to string
            plate = "".join(pList)
            plates.append(plate)
            print("New plate generated: ", plate)
            x = x + 1
    # print("Generated plates below")
    # print(plates)
else:
    # display if inputed LGI is not in list
    print("This LGI does not exist")