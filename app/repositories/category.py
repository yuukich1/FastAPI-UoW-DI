from app.models.models import Category
from app.utils.repository import SQLAlchemyRepository

class CategoryRepository(SQLAlchemyRepository):

    model = Category