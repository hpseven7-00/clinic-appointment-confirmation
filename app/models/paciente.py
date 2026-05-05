from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)  # Formato: 5599999999999