from app.models.models import ProductsImage
from app.utils.repository import SQLAlchemyRepository

class ProductImageRepository(SQLAlchemyRepository):

    model = ProductsImage