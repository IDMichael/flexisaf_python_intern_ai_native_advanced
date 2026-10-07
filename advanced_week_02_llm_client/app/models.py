from pydantic import BaseModel, Field

class SummaryResult(BaseModel):
    """Typed contract returned by the summarisation operation."""
    summary: str = Field(min_length=1)
    key_points: list[str] = Field(min_length=1, max_length=5)
