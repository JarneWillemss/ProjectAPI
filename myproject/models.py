from database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class SupplementCompany(Base):
    __tablename__ = "supplement_companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    items = relationship("Item", back_populates="company")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    company_id = Column(Integer, ForeignKey("supplement_companies.id"))
    company = relationship("SupplementCompany", back_populates="items")