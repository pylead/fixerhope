import dataclasses
import typing as t
import uuid

from app.dto.missing import MISSING


@dataclasses.dataclass
class FilterParams:
    id: t.Optional[uuid.UUID] = MISSING
    id__in: t.Optional[t.List[uuid.UUID]] = MISSING

    @classmethod
    def __class_getitem__(cls, *required: t.Tuple) -> t.Type['FilterParams']:
        # TODO: unmake field optional if it's required & return new dataclass
        return cls
