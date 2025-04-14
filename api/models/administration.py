from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Administration(Base):
    __tablename__ = "administration"

    admin_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)