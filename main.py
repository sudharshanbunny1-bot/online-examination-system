"""
CLI entry point for Online Examination System.
"""
from exam_core import Exam, Question

def get_sample_exam() -> Exam:
    questions = [
        Question(1, "What is Git?", ["A version control system", "A programming language", "An operating system", "A cloud server"], 0, 2),
        Question(2, "Which command creates a new branch and switches to it?", ["git switch", "git checkout -b", "git branch new", "git merge"], 1, 2),
        Question(3, "Which tool isolates the first bad commit?", ["git bisect", "git log", "git rebase", "git checkout"], 0, 2)
    ]
    return Exam(title="Git & Version Control Fundamentals", duration_minutes=15, passing_percentage=60.0, questions=questions)

def run():
    exam = get_sample_exam()
    print(f"--- {exam.title} ---")
    print(f"Total Questions: {len(exam.questions)} | Max Marks: {exam.total_marks()}")
    answers = {1: 0, 2: 1, 3: 0}
    result = exam.evaluate(answers)
    print(f"Score: {result['score']}/{result['total_marks']} ({result['percentage']}%) - Passed: {result['passed']}")

if __name__ == "__main__":
    run()
