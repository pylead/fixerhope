import dataclasses
import typing as t


@dataclasses.dataclass
class ScopeParams:
    fields: t.Optional[t.List[str]] = None
