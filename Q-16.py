# Calculate Body Mass Index (BMI)
# Input weight (kg) and height (m), then calculate:
# BMI = weight / (height ** 2


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", bmi)