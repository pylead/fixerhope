import dataclasses
import typing as t


@dataclasses.dataclass
class PagingParams:
    limit: t.Optional[int] = 20
    offset: t.Optional[int] = 0
