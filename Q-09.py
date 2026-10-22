# Question 9:# Total Marks and Percentage
# Input marks of 5 subjects. Print:
#  Total marks
#  Percentage
#  Average


English = int(input("Enter the english marks:  "))
Urdu = int(input("Enter the urdu marks:  "))
Math = int(input("Enter the math marks:  "))
Computer = int(input("Enter the computer marks:  "))
Islamiat = int(input("Enter the islamiat marks:  "))
print("   ")

total1 = English + Urdu + Math + Computer + Islamiat
percentage = (total1 / 500)*100
average = (total1 / 5)


print("Total marks:",  total1)
print("Percentage:",     percentage)
print("Average:",    average)
print("  ")

if percentage >= 80:
    print("Remarks: Excellent")
elif percentage >= 60:
    print("Remarks: Good")
else:
    print("Remarks: Need improvement")


