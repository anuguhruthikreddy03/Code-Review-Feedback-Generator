from pydantic import BaseModel
from typing import List

class CodeReview(BaseModel):
    identified_issues: List[str]
    improvement_suggestions: List[str]
    code_quality_level: str
    review_summary: str