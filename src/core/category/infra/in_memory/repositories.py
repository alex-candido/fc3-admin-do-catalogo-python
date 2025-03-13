from typing import List
from core.category.domain.entities import Category
from core.category.domain.repositories import CategoryRepository
from core.__seedwork.domain.repositories import InMemoryRepository

class CategoryInMemoryRepository(CategoryRepository, InMemoryRepository):
    pass