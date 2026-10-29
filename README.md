# AI-Based Student Performance Predictor

A beginner-friendly Python application illustrating the foundational Artificial Intelligence concept of **Rule-Based Systems** (also known as *Expert Systems* or *Production Systems*).

---

## 🧠 AI Concept: Rule-Based Systems

A **Rule-Based System** is one of the earliest and most transparent forms of Artificial Intelligence. Instead of learning patterns from statistical training data (like modern Machine Learning or Deep Learning), it solves problems by applying human-curated expert knowledge in the form of **IF-THEN** rules.

A standard Rule-Based AI architecture consists of three components:

```
+-------------------------------------------------------+
|                    WORKING MEMORY                     |
|  (Stores inputs & current facts: hours & attendance)  |
+---------------------------+---------------------------+
                            |
                            v
+-------------------------------------------------------+
|                   INFERENCE ENGINE                    |
| (Matches facts from memory against rules to decide)   |
+---------------------------+---------------------------+
                            ^
                            |
+---------------------------+---------------------------+
|                    KNOWLEDGE BASE                     |
|  (Contains domain expertise as IF-THEN rules)         |
+-------------------------------------------------------+
```

1. **Knowledge Base (Rules)**: The domain rules defined by human educators.
   - **Rule 1**: IF `study_hours >= 2` AND `attendance >= 75` $\rightarrow$ "Good Preparation"
   - **Rule 2**: IF `study_hours >= 1` AND `attendance >= 60` $\rightarrow$ "Needs Improvement"
   - **Rule 3**: ELSE $\rightarrow$ "More Preparation Required"
2. **Working Memory (Facts)**: The input data provided by the student (`study_hours` and `attendance`).
3. **Inference Engine**: The logical reasoning module (`evaluate_performance()`) that matches facts against rules to deduce recommendations.

---

## 🚀 Features

- **Beginner-Friendly Modular Architecture**: Separates input handling, inference logic, and output formatting.
- **Robust Input Validation**:
  - Catches non-numeric inputs (e.g. text or symbols) with `try-except` blocks.
  - Validates logical boundaries (Study Hours: `0 - 24`, Attendance: `0 - 100%`).
  - Automatically re-prompts the user until valid data is provided without crashing.

---

## 🛠️ How to Run

### Prerequisites
- Python 3.10+ installed on your computer.

### Running the Program
Open a terminal / PowerShell in this directory and run:

```bash
python student_performance_predictor.py
```

---

## 📋 Example Runs

### Example 1: Good Preparation
```text
===================================
  STUDENT PERFORMANCE PREDICTOR
===================================
Enter daily study hours (0 - 24): 3.5
Enter attendance percentage (0 - 100): 88

-----------------------------------
Prediction: Good Preparation
Recommendation: Keep up your good work!
-----------------------------------

Thank you for using the predictor!
```

### Example 2: Needs Improvement
```text
===================================
  STUDENT PERFORMANCE PREDICTOR
===================================
Enter daily study hours (0 - 24): 1.5
Enter attendance percentage (0 - 100): 65

-----------------------------------
Prediction: Needs Improvement
Recommendation: Study regularly and improve attendance.
-----------------------------------

Thank you for using the predictor!
```

### Example 3: Error Handling & Out-of-Range Recovery
```text
===================================
  STUDENT PERFORMANCE PREDICTOR
===================================
Enter daily study hours (0 - 24): abc
Error: Invalid numerical input. Please enter a valid number.
Enter daily study hours (0 - 24): 25
Error: Value must be between 0.0 and 24.0. Please try again.
Enter daily study hours (0 - 24): 2.0
Enter attendance percentage (0 - 100): 110
Error: Value must be between 0.0 and 100.0. Please try again.
Enter attendance percentage (0 - 100): 80

-----------------------------------
Prediction: Good Preparation
Recommendation: Keep up your good work!
-----------------------------------

Thank you for using the predictor!
```
