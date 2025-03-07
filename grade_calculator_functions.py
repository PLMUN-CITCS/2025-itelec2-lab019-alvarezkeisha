

def get_student_score() -> float:
    """
    Prompts the user to enter their score and returns it as a numerical value.
    Ensures the input is valid and returns a numeric score.
    
    Returns:
        float: The student's score entered by the user.
    """
    while True:
        try:
            # Prompt the user to enter a score
            score = float(input("Enter your score: "))
            
            # Ensure score is within a valid range
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score.

    Args:
        score (float): The student's score.

    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    """
    Main function to run the grade calculator program.
    It calls get_student_score() to get the score, calculates the grade,
    and then displays the result.
    """
    score = get_student_score()  # Get the student's score
    grade = calculate_grade(score)  # Calculate the grade based on the score
    print(f"Your Grade is: {grade}")  # Display the grade to the user

# Call the main function to run the program
if __name__ == "__main__":
    main()
