# This program calculates a letter grade from a score.

# First, we need to ask the user for their score.
score = input("Enter your score: ")

# We need to change the score from text to a number.
score = int(score)  # Converts the input to an integer (whole number)

# Now, we check the score and decide the grade.
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Finally, we tell the user their grade.
print("Your Grade is:", grade)
