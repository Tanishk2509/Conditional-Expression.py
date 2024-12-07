marks1 = int(input("Enter you marks 1: "))
marks2 = int(input("Enter you marks 2: "))
marks3 = int(input("Enter you marks 3: "))

#check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/3

if(total_percentage>=40):
    print("you are pass:", total_percentage)

else:
    print("you failed, try again next year:", total_percentage)



              