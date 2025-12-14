from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class PromptTemplate(BaseModel):
    name: str
    description: str
    pattern: str
    input_variables: List[str]
    template: str
    examples: Optional[List[Dict[str, Any]]] = None
