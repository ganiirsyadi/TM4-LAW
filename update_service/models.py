from os import fwalk
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Mahasiswa(Base):
    __tablename__ = "mahasiswa"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    npm = Column(String(10), unique=True, nullable=False, index=True)
    nama = Column(String(255), unique=False, nullable=False, index=True)
    def __str__(self):
        return f"Mahasiswa(npm={self.npm}, nama={self.nama})"