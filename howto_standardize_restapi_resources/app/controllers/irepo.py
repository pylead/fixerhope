import typing as t

from app import dto, entities


class IRepo:
    entity_class: t.ClassVar[t.Type[entities.IEntity]] = entities.IEntity

    def get_count(
        self,
        filter_params: t.Optional[dto.FilterParams] = None,
    ) -> int:
        raise NotImplementedError

    def get_list(
        self,
        filter_params: t.Optional[dto.FilterParams] = None,
        scope_params: t.Optional[dto.ScopeParams] = None,
        order_params: t.Optional[dto.OrderParams] = None,
        paging_params: t.Optional[dto.PagingParams] = None,
    ) -> t.List['entity_class']:
        raise NotImplementedError

    def get_dict(
        self,
        filter_params: t.Optional[dto.FilterParams] = None,
        scope_params: t.Optional[dto.ScopeParams] = None,
        order_params: t.Optional[dto.OrderParams] = None,
        paging_params: t.Optional[dto.PagingParams] = None,
    ) -> t.Dict[t.Type['entity_class.id'], 'entity_class']:
        raise NotImplementedError

    def get_item(
        self,
        filter_params: dto.FilterParams['id'],
        scope_params: t.Optional[dto.ScopeParams] = None,
    ) -> t.List['entity_class']:
        raise NotImplementedError

    def create_list(
        self,
        items_list: t.List['entity_class'],
    ) -> t.List['entity_class']:
        raise NotImplementedError

    def create_item(self, item: 'entity_class') -> 'entity_class':
        raise NotImplementedError

    def update_list(
        self,
        items_list: t.List['entity_class'],
    ) -> t.List['entity_class']:
        raise NotImplementedError

    def update_item(self, item: 'entity_class') -> 'entity_class':
        raise NotImplementedError

    def delete_list(self, filter_params: dto.FilterParams) -> int:
        raise NotImplementedError
