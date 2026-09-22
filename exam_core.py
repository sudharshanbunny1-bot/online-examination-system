"""
Core logic and models for the Online Examination System.
"""
from dataclasses import dataclass
from typing import List, Dict, Optional
import time

@dataclass
class Question:
    id: int
    prompt: str
    options: List[str]
    correct_option_index: int
    marks: int = 1

    def is_correct(self, selected_index: int) -> bool:
        return selected_index == self.correct_option_index


@dataclass
class Exam:
    title: str
    duration_minutes: int
    passing_percentage: float
    questions: List[Question]

    def total_marks(self) -> int:
        return sum(q.marks for q in self.questions)

    def evaluate(self, answers: Dict[int, int]) -> Dict[str, any]:
        score = 0
        details = []
        for q in self.questions:
            selected = answers.get(q.id)
            correct = q.is_correct(selected) if selected is not None else False
            earned = q.marks if correct else 0
            score += earned
            details.append({
                "question_id": q.id,
                "selected": selected,
                "correct": correct,
                "earned_marks": earned
            })
        
        total = self.total_marks()
        percentage = (score / total * 100.0) if total > 0 else 0.0
        passed = percentage >= self.passing_percentage
        
        return {
            "score": score,
            "total_marks": total,
            "percentage": round(percentage, 2),
            "passed": passed,
            "details": details
        }
