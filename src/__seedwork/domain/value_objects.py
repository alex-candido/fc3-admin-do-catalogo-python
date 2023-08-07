import uuid
from dataclasses import dataclass, field

from __seedwork.domain.exceptions import InvalidUuidException


@dataclass(frozen=True, slots=True)
class UniqueEntityId:
  id: str = field(  # pylint: disable=invalid-name
        default_factory=lambda: str(uuid.uuid4())
    )
  
  def __validate(self):
      try:
          uuid.UUID(self.id)
      except ValueError as ex:
          raise InvalidUuidException() from ex