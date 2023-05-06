from sqlalchemy import create_engine,  Table, Column, Integer, String, Double, Identity
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import insert, select



class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "Products"

    ProductId: Mapped[int] = mapped_column(Identity(), primary_key=True)
    ProductName: Mapped[str] = mapped_column(nullable=False)
    ProductType: Mapped[str] = mapped_column(nullable=False)
    UnitPrice: Mapped[float] = mapped_column(nullable=False)
    Currency: Mapped[str] = mapped_column(nullable=False)


class Client(Base):
    __tablename__ = "Clients"

    ClientId: Mapped[int] = mapped_column(Identity(), primary_key=True)
    ClientName: Mapped[str] = mapped_column(nullable=False)
    DeliveryAddress: Mapped[str] = mapped_column(nullable=False)
    DeliveryCity: Mapped[str] = mapped_column(nullable=False)
    DeliveryPostcode: Mapped[str] = mapped_column(nullable=False)
    DeliveryCountry: Mapped[str] = mapped_column(nullable=False)
    DeliveryContactNumber: Mapped[str]






