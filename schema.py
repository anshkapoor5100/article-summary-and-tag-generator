from pydantic import BaseModel, Field
from typing import Annotated, List
class AnalysisResult(BaseModel):
    summary: Annotated[str,Field(description="summay of given query")]
    key_entities:List[str]
    confidence_score:Annotated[int,Field(gt=0, le=10)]