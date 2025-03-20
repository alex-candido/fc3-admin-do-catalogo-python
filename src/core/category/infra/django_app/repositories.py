# pylint: disable=no-member,unexpected-keyword-arg
from typing import List, Type, TYPE_CHECKING
from django.core import exceptions as django_exceptions
from django.core.paginator import Paginator
from core.__seedwork.domain.exceptions import NotFoundException
from core.__seedwork.domain.value_objects import UniqueEntityId
from core.category.domain.entities import Category
from core.category.domain.repositories import CategoryRepository


if TYPE_CHECKING:
    from core.category.infra.django_app.models import CategoryModel


class CategoryDjangoRepository(CategoryRepository):
    
    def insert(self, category: Category) -> Category:
        CategoryModel.objects.create(**category.to_dict())
    
    def find_by_id(self, entity_id: str | UniqueEntityId) -> Category:
        id_str = str(entity_id)
        model = self._get(id_str)
        return Category(unique_entity_id=UniqueEntityId(id_str), **model.to_dict())
    
    def find_all(self) -> List[Category]:
        raise NotImplementedError()
    
    def update(self, category: Category) -> None:
        raise NotImplementedError()
    
    def delete(self, entity_id: str | UniqueEntityId) -> None:
        raise NotImplementedError()
    
    def _get(self, entity_id: str) -> 'CategoryModel':
        try:
            return CategoryModel.objects.get(pk=entity_id)
        except (CategoryModel.DoesNotExist, django_exceptions.ValidationError) as exception:
            raise NotFoundException(
                f"Entity not found using ID '{entity_id}'") from exception
    
    def search(self, input_params: CategoryRepository.SearchParams) -> CategoryRepository.SearchResult:
        raise NotImplementedError()
    
