# Percentage of Correct Answers
# Input total questions and correct answers, and calculate the 
# percentage score

total_questions = int(input("Enter total questions:  "))
correct_answers = int(input("Enter correct answers"))
percentage = (correct_answers / total_questions) * 100
print("Percentage:", percentage, "%")