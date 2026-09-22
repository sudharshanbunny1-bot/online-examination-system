"""
Authentication and session management for students and examiners.
"""
import hashlib
from typing import Dict, Optional

class AuthService:
    def __init__(self):
        # In-memory user store: username -> (hashed_password, role)
        self._users: Dict[str, tuple[str, str]] = {}
        self._active_sessions: set[str] = set()

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def register_user(self, username: str, password: str, role: str = "student") -> bool:
        if username in self._users:
            return False
        self._users[username] = (self._hash_password(password), role)
        return True

    def login(self, username: str, password: str) -> Optional[dict]:
        if username not in self._users:
            return None
        hashed, role = self._users[username]
        if hashed == self._hash_password(password):
            token = f"session_{username}_{hashlib.md5(username.encode()).hexdigest()[:8]}"
            self._active_sessions.add(token)
            return {"username": username, "role": role, "session_token": token}
        return None

    def logout(self, token: str) -> bool:
        if token in self._active_sessions:
            self._active_sessions.remove(token)
            return True
        return False
