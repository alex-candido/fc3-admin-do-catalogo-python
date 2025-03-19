from typing import Callable
from dataclasses import asdict, dataclass
from urllib.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request as DrfRequest
from rest_framework import status as http
from core.category.application.use_cases import (
    CreateCategoryUseCase,
    ListCategoriesUseCase,
)
from core.category.infra.in_memory.repositories import CategoryInMemoryRepository
# testes end to end - funcionamento
# testes integração -
# testes unitários controllers -

@dataclass(slots=True)
class CategoryResource(APIView):

    create_use_case: CreateCategoryUseCase

    def post(self, request: Request):
      input_param = CreateCategoryUseCase.Input(name=request.data['name'])
      output = self.create_use_case.execute(input_param)
      return Response(asdict(output))
