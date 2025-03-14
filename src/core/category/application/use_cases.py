
# pylint: disable=unexpected-keyword-arg
from dataclasses import dataclass, asdict
from typing import Optional
from core.__seedwork.application.dto import PaginationOutput, PaginationOutputMapper, SearchInput
from core.__seedwork.application.use_cases import UseCase
from core.category.domain.entities import Category
from core.category.domain.repositories import CategoryRepository
from core.category.application.dto import CategoryOutput, CategoryOutputMapper

@dataclass(slots=True, frozen=True)
class CreateCategoryUseCase():
    
    category_repo: CategoryRepository
    
    def execute(self, input_param: 'Input') -> 'Output':
        category = Category(
            name=input_param.name,
            description=input_param.description,
            is_active=input_param.is_active
        )
        
        self.category_repo.insert(category)
        return self.__to_output(category)
    
    @dataclass(slots=True, frozen=True)
    class Input:
        name: str
        description: Optional[str] = Category.get_field('description').default
        is_active: Optional[bool] = Category.get_field('is_active').default
        
    @dataclass(slots=True, frozen=True)
    class Output(CategoryOutput):
        pass
    
