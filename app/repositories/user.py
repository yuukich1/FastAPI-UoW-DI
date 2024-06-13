from app.models.models import Users
from app.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    
    model = Users