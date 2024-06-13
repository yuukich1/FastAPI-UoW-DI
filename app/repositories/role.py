from app.models.models import Roles
from app.utils.repository import SQLAlchemyRepository

class RolesRepository(SQLAlchemyRepository):
    
    model = Roles