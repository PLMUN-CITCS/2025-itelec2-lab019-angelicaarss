# grade_calculator_functions.py

def get_student_score():
    """
    Prompts the user to enter their score and returns it as a numerical value.
    """
    while True:
        try:
            score = float(input("Enter your score: "))  # Allow for float scores
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical score.")

def calculate_grade(score):
    """
    Calculates the letter grade based on the given score.

    Args:
        score (float): The student's score.

    Returns:
        str: The corresponding letter grade.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    """
    Main program flow: gets score, calculates grade, and displays the result.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()
