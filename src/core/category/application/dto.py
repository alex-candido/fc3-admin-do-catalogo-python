from dataclasses import dataclass
from datetime import datetime
from typing import Optional, TypeVar
from core.category.domain.entities import Category

@dataclass(frozen=True, slots=True)
class CategoryOutput:
    id: str  # pylint: disable=invalid-name
    name: str
    description: Optional[str]
    is_active: bool
    created_at: datetime