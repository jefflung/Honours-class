#honours classification

firstName=str(input("Please enter your first name:"))
lastName=str(input("Please enter your last name:"))
wam=int(input("Please enter your Weighted Average Mark:"))

if(wam>=0 and wam<=100):
    
    if(wam>=70):
        classification="First Class"
        message="Excellent, well done!"
        print(firstName+" "+lastName)
        print("Your Honours Classification is",classification)
    elif(wam>=60):
        classification="Upper Second"
        message="Very good, well done!"
        print(firstName+" "+lastName)
        print("Your Honours Classification is",classification)
    elif(wam>=50):
        classification="Lower Second"
        message="Good, well done!"
        print(firstName+" "+lastName)
        print("Your Honours Classification is",classification)
    elif(wam>=40):
        classification="Third Class"
        message="Could have done better!"
        print(firstName+" "+lastName)
        print("Your Honours Classification is",classification)
    elif(wam>=35):
        classification="Pass Degree"
        message="Work harder next time!"
        print(firstName+" "+lastName)
        print("Your Honours Classification is",classification)
    else:
        classification="Fail"
        message="Oh dear, try again!"
        print(firstName+" "+lastName)
        print("Your Honours Classification is",classification)
else:
    message="The input is invalid."

print(message)