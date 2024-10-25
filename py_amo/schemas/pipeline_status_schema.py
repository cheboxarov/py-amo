from typing import Optional, List
from pydantic import BaseModel, Field

class PipelineStatusDescriptionSchema(BaseModel):
    id: Optional[int] = None
    account_id: Optional[int] = None
    created_at: Optional[str] = None  # В формате YYYY-MM-DD HH:MM:SS
    updated_at: Optional[str] = None  # В формате YYYY-MM-DD HH:MM:SS
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    pipeline_id: Optional[int] = None
    status_id: Optional[int] = None
    level: Optional[str] = None
    description: Optional[str] = None

class PipelineStatusSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    sort: Optional[int] = None
    is_editable: Optional[bool] = None
    pipeline_id: Optional[int] = None
    color: Optional[str] = None
    type: Optional[int] = None
    account_id: Optional[int] = None
    descriptions: Optional[List[PipelineStatusDescriptionSchema]] = None