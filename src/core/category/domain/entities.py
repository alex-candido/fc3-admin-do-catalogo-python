from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from core.__seedwork.domain.entities import Entity
from core.__seedwork.domain.value_objects import UniqueEntityId

@dataclass(kw_only=True, frozen=True, slots=True) #init, repr, eq
class Category(Entity):
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now()
      )
  
# piramide de testes
# testes de unidades
# testes de integração
# testes e2e

# Michael Feathers


# POST /categories - controller - usecase -> { name: "256" , invalidas} -> entidade

# Notification Pattern - Martin Fowler
# lib - Limite Parcial da Arquitetura

# required, max, positive, negativo, email, uuid, cartao de credito