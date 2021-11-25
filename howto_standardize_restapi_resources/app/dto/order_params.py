import dataclasses
import enum
import typing as t


class Order(enum.IntEnum):
    asc = 1
    desc = -1


@dataclasses.dataclass
class Field:
    Order: t.ClassVar[t.Type[Order]] = Order

    name: str
    order: t.Optional['Order'] = Order.asc

    def asc(self) -> 'Field':
        return Field(name=self.name, order=Order.asc)

    def desc(self) -> 'Field':
        return Field(name=self.name, order=Order.desc)


@dataclasses.dataclass
class OrderParams:
    Field: t.ClassVar[t.Type[Field]] = Field

    fields: t.Optional[t.List['Field']] = None
