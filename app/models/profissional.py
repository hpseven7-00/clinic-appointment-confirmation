from sqlalchemy import Column, Integer, String
from models.base import Base

class Profissional(Base):
    __tablename__ = "profissionais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String)  # Ex: Fisioterapeuta, Psicólogo