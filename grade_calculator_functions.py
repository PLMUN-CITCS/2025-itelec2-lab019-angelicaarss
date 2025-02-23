def get_student_score() -> int:
    """
    Prompts the user to enter their score and returns it as an integer.

    Returns:
        int: The student's score.
    """
    while True:
        try:
            score = int(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical score.")

def calculate_grade(score: int) -> str:
    """
    Calculates the grade based on the given score.

    Args:
        score (int): The student's score.

    Returns:
        str: The calculated grade.
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
    Main function to orchestrate the program.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()