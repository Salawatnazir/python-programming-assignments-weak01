#Question 7:
# Distribute Items Equally - You have n candies and k students.
#Write a program to find:
#how many candies each student gets
#how many are left

n = int(input("Enter the total number of candies"))
k = int(input("Enter the total number of students"))
each = n//k
print("each student gets:", each)
left =n%k
print("candies left:",left)
