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
    pass
