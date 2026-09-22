"""
Timer utility for monitoring examination time limits and triggering auto-submission.
"""
import time

class ExamTimer:
    def __init__(self, duration_minutes: int):
        self.duration_seconds = duration_minutes * 60
        self.start_time: Optional[float] = None

    def start(self):
        self.start_time = time.time()

    def elapsed_seconds(self) -> float:
        if self.start_time is None:
            return 0.0
        return time.time() - self.start_time

    def remaining_seconds(self) -> float:
        remaining = self.duration_seconds - self.elapsed_seconds()
        return max(0.0, remaining)

    def is_expired(self) -> bool:
        return self.remaining_seconds() <= 0.0
