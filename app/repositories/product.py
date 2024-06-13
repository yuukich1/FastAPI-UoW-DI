from app.models.models import Products
from app.utils.repository import SQLAlchemyRepository

class ProductRepository(SQLAlchemyRepository):

    model = Products