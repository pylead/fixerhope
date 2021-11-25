import typing as t

import marshmallow as ma
from flask_restful import Resource

from app.controllers.irepo import IRepo


class RepoResource(Resource):
    filter_params_schema: t.ClassVar[t.Type[ma.Schema]] = ma.Schema
    scope_params_schema: t.ClassVar[t.Type[ma.Schema]] = ma.Schema
    order_params_schema: t.ClassVar[t.Type[ma.Schema]] = ma.Schema
    paging_params_schema: t.ClassVar[t.Type[ma.Schema]] = ma.Schema
    repo_class: t.ClassVar[t.Type[IRepo]] = IRepo
