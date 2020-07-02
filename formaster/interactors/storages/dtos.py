from dataclasses import dataclass
from typing import Optional, List

@dataclass()
class FormDto:
    form_id: int
    is_live: bool

@dataclass()
class UserMCQResponseDTO:
    user_id: int
    question_id: int
    user_submitted_option_id: int

@dataclass()
class UserFillInTheBlankResponseDTO:
    user_id: int
    question_id: int
    user_submitted_text: str