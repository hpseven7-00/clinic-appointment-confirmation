from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Sessao(Base):
    __tablename__ = "sessoes"

    id = Column(Integer, primary_key=True, index=True)
    data_horario = Column(DateTime, nullable=False)
    # Status: 'Pendente', 'Confirmado', 'Cancelado' ou 'Não Respondido'
    status = Column(String, default="Pendente") 

    # Chaves Estrangeiras (Relacionamentos)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    profissional_id = Column(Integer, ForeignKey("profissionais.id"))

    # Atalhos para acessar os objetos ligados
    paciente = relationship("Paciente")
    profissional = relationship("Profissional")