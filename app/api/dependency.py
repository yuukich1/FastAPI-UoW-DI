from fastapi import Depends
from typing import Annotated
from app.utils.unitofwork import IUnitOfWork, UnitOfWork


UOWdep = Annotated[UnitOfWork, Depends(UnitOfWork)]