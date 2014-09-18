#Callum Brown
#18-09-14
#binary to denary- Task 1

binary = input("Please could you enter your binary number: ")
total = 0

if binary[0] == "1":
   total = total +8
if binary[1] == "1":
   total = total +4
if binary[2] == "1":
   total =  total +2
if binary[3] == "1":
   total = total +1

print("Your denary number is: {0}".format(total))



