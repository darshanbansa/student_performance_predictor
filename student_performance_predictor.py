"""
AI-Based Student Performance Predictor
Demonstration of a Rule-Based System in Python.

This program evaluates a student's daily study hours and attendance percentage
to provide a performance-related prediction and recommendation.
"""


def get_valid_float(prompt: str, min_val: float, max_val: float) -> float:
    """
    Prompt the user repeatedly until a valid floating-point number
    within [min_val, max_val] is provided.
    
    Handles non-numeric values gracefully using try-except.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            val = float(user_input)
            if min_val <= val <= max_val:
                return val
            print(f"Error: Value must be between {min_val} and {max_val}. Please try again.")
        except ValueError:
            print("Error: Invalid numerical input. Please enter a valid number.")


def evaluate_performance(study_hours: float, attendance: float) -> tuple[str, str]:
    """
    Inference Engine:
    Applies production rules (IF-THEN conditions) to inputs in Working Memory
    to determine the prediction and actionable recommendation.
    
    Rules:
      - Rule 1: IF study_hours >= 2.0 AND attendance >= 75.0
                THEN "Good Preparation", "Keep up your good work!"
      - Rule 2: IF study_hours >= 1.0 AND attendance >= 60.0
                THEN "Needs Improvement", "Study regularly and improve attendance."
      - Rule 3: ELSE
                THEN "More Preparation Required", "Increase study time and attend classes regularly."
    """
    if study_hours >= 2.0 and attendance >= 75.0:
        return "Good Preparation", "Keep up your good work!"
    elif study_hours >= 1.0 and attendance >= 60.0:
        return "Needs Improvement", "Study regularly and improve attendance."
    else:
        return "More Preparation Required", "Increase study time and attend classes regularly."


def main() -> None:
    """Main execution flow for the Student Performance Predictor."""
    print("===================================")
    print("  STUDENT PERFORMANCE PREDICTOR")
    print("===================================")

    # Gather inputs with robust boundary & type validation
    study_hours = get_valid_float("Enter daily study hours (0 - 24): ", 0.0, 24.0)
    attendance = get_valid_float("Enter attendance percentage (0 - 100): ", 0.0, 100.0)

    # Pass inputs through the Rule-Based Inference Engine
    prediction, recommendation = evaluate_performance(study_hours, attendance)

    # Display results
    print("\n-----------------------------------")
    print(f"Prediction: {prediction}")
    print(f"Recommendation: {recommendation}")
    print("-----------------------------------")
    print("\nThank you for using the predictor!")


if __name__ == "__main__":
    main()
