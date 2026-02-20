from sqlalchemy import BigInteger
from db import Base
from sqlalchemy.orm import Mapped, mapped_column


class Country(Base):
    __tablename__ = "countries"

    country: Mapped[str] = mapped_column(nullable=False)
    region: Mapped[str] = mapped_column(nullable=False)
    population: Mapped[int] = mapped_column(BigInteger, nullable=False)
