import dataclasses
import uuid


@dataclasses.dataclass
class IEntity:
    id: uuid.UUID
