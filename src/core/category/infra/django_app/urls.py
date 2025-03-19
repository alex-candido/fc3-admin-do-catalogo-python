
from dataclasses import dataclass
from django.urls import path  # pylint: disable=import-self
from core.category.application.use_cases import CreateCategoryUseCase
from core.category.infra.in_memory.repositories import CategoryInMemoryRepository
from django_app import container
from .api import CategoryResource

@dataclass()
class CategoryInMemoryRepositoryFactory:

    repo: CategoryInMemoryRepository = None

    @classmethod
    def create(cls):
      if not cls.repo:
        cls.repo = CategoryInMemoryRepository()
      return cls.repo

class CreateCategoryUseCaseFactory:

    @classmethod
    def create(cls):
      repo = CategoryInMemoryRepositoryFactory.create()
      return CreateCategoryUseCase(repo)

urlpatterns = [
    path('categories/', CategoryResource.as_view(
        create_use_case=CreateCategoryUseCaseFactory.create())
    ),
    path('categories/<id>/', CategoryResource.as_view())
]
