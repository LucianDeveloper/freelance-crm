from ..storage.services import product_s
from .schemas import SchemaFilterProducts


class Finder:
    @staticmethod
    async def get_products_by_filter(filters: SchemaFilterProducts):
        return await product_s.filter(
            **{x: y for x, y in filters.dict().items() if y is not None}
        )
