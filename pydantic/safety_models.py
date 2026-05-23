from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
import re

class PromptSafety(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=2000)
    model_name: str = Field(..., pattern=r'^[a-zA-Z0-9_.-]+$')
    temperature: float = Field(0.0, ge=0.0, le=1.0)
    max_tokens: int = Field(100, ge=1, le=4096)

    @field_validator('prompt')
    def validate_safety(cls, v):
        harmful_patterns = [
            r'(?i)bomb|hack|exploit|malware|virus',
            r'(?i)override.*safety|ignore.*rules|jailbreak'
        ]
        for pattern in harmful_patterns:
            if re.search(pattern, v):
                raise ValueError('Prompt contains potentially harmful content')
        return v

class ResponseSafety(BaseModel):
    content: str
    risk_score: float = Field(..., ge=0.0, le=1.0)
    flagged_categories: List[str] = Field(default_factory=list)

    @field_validator('content')
    def check_toxicity(cls, v):
        if len(v) > 5000:
            raise ValueError('Response too long')
        return v