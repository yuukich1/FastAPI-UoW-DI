from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import ForeignKey
from app.schemas.category import CategoryScheme
from app.schemas.product import ProductScheme, ProductImageScheme
from app.schemas.users import RoleScheme, UserScheme
from app.schemas.order import OrderScheme, StatusOrderScheme
from datetime import datetime, timezone


class Base(DeclarativeBase):
    ...


class Category(Base):
    __tablename__ = 'Category'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str]
    image: Mapped[str] = mapped_column(default='placeholder.png')

    def to_read_model(self) -> CategoryScheme:
        return CategoryScheme(id = self.id,
                              name = self.name,
                              description = self.description,
                              image = self.image
                              )


class Products(Base):
    __tablename__ = 'Products'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    category_id : Mapped[int] = mapped_column(ForeignKey(Category.id), nullable=True)

    def to_read_model(self) -> ProductScheme:
        return ProductScheme(id = self.id, 
                             name = self.name,
                             description = self.description
                             )


class ProductsImage(Base):
    __tablename__ = 'ProductsImage'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    image: Mapped[str] = mapped_column(nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey(Products.id), nullable=False)

    def to_read_model(self) -> ProductImageScheme:
        return ProductImageScheme(id = self.id,
                                  image = self.image,
                                  product_id= self.product_id
                                  )


class Roles(Base):
    __tablename__ = 'Roles'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    def to_read_model(self) -> RoleScheme:
        return RoleScheme(id = self.id,
                          name = self.name
                          )


class Users(Base):
    __tablename__ = 'Users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    active: Mapped[bool] = mapped_column(default=False)
    date_registaration: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
    role_id: Mapped[int] = mapped_column(ForeignKey(Roles.id), nullable=False, default=1)

    def to_read_model(self) -> UserScheme:
        return UserScheme(id = self.id,
                          username = self.username,
                          email = self.email,
                          password = self.password,
                          active = self.active,
                          date_registration= self.date_registaration,
                          role_id = self.role_id
                          )


class StatusOrder(Base):
    __tablename__ = 'StatusOrder'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    def to_read_model(self) -> StatusOrderScheme:
        return StatusOrderScheme(id = self.id,
                                 name = self.name)



class Order(Base):
    __tablename__ = 'Order'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(Users.id), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey(Products.id), nullable=False)
    status_id: Mapped[int] = mapped_column(ForeignKey(StatusOrder.id), nullable=True)
    date_order: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)

    def to_read_model(self):
        return OrderScheme(id = self.id,
                           user_id = self.user_id,
                           product_id = self.product_id,
                           status_id = self.status_id,
                           date_order = self.date_order
                           )
    

