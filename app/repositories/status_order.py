from app.models.models import StatusOrder
from app.utils.repository import SQLAlchemyRepository

class StatusOrderRepository(SQLAlchemyRepository):

    model = StatusOrder