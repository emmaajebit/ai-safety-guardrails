from pydantic import BaseModel, Field, validator
from typing import List, Optional

class AISafetyInput(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=10000)
    model: str = Field(..., pattern=r'^[a-zA-Z0-9-]+$')
    safety_level: str = Field(default='medium', pattern='^(low|medium|high)$')

    @validator('prompt')
    def validate_no_harmful_content(cls, v):
        harmful_keywords = ['hack', 'exploit', 'malware']
        if any(kw in v.lower() for kw in harmful_keywords):
            raise ValueError('Potentially harmful content detected')
        return v

# Example usage
if __name__ == "__main__":
    try:
        input_data = AISafetyInput(prompt="Safe AI query", model="gpt-4")
        print("Validation passed")
    except ValueError as e:
        print(f"Validation failed: {e}")