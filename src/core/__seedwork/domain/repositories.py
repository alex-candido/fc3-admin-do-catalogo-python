from abc import ABC
import abc
from ast import Delete
from dataclasses import dataclass, field
import math
from typing import Any, Generic, List, Optional, TypeVar
from core.__seedwork.domain.value_objects import UniqueEntityId
from core.__seedwork.domain.entities import Entity
from core.__seedwork.domain.exceptions import NotFoundException

ET = TypeVar('ET', bound=Entity)

class RepositoryInterface(Generic[ET], ABC):

    @abc.abstractmethod
    def insert(self, entity: ET) -> None:
        raise NotImplementedError()

    def bulk_insert(self, entities: List[ET]) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_id(self, entity_id: str | UniqueEntityId) -> ET:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_all(self) -> List[ET]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, entity: ET) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, entity_id: str | UniqueEntityId) -> None:
        raise NotImplementedError()
    
Input = TypeVar('Input')
Output = TypeVar('Output')


class SearchableRepositoryInterface(Generic[ET, Input, Output], RepositoryInterface[ET], ABC):

    sortable_fields: List[str] = []

    @abc.abstractmethod
    def search(self, input_params: Input) -> Output:
        raise NotImplementedError()

@dataclass(slots=True)
class InMemoryRepository(RepositoryInterface[ET], ABC):
    items: List[ET] = field(default_factory=lambda: [])

    def insert(self, entity: ET) -> None:
        self.items.append(entity)

    def bulk_insert(self, entities: List[ET]) -> None:
        self.items = entities + self.items

    def find_by_id(self, entity_id: str | UniqueEntityId) -> ET:
        id_str = str(entity_id)
        return self._get(id_str)

    def find_all(self) -> List[ET]:
        return self.items

    def update(self, entity: ET) -> None:
        entity_found = self._get(entity.id)
        index = self.items.index(entity_found)
        self.items[index] = entity

    def delete(self, entity_id: str | UniqueEntityId) -> None:
        id_str = str(entity_id)
        entity_found = self._get(id_str)
        self.items.remove(entity_found)

    def _get(self, entity_id: str) -> ET:
        entity = next(filter(lambda i: i.id == entity_id, self.items), None)
        if not entity:
            raise NotFoundException(f"Entity not found using ID '{entity_id}'")
        return entity
