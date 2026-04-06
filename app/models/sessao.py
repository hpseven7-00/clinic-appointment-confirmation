from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Sessao(Base):
    __tablename__ = "sessoes"

    id = Column(Integer, primary_key=True, index=True)
    data_hora_sessao = Column(DateTime, nullable=False)
    # Status: 'Pendente', 'Confirmado', 'Cancelado' ou 'Não Respondido'
    status = Column(String, default="Pendente")
    telefone = Column(String, nullable=False)

    # Chaves Estrangeiras (Relacionamentos)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    profissional_id = Column(Integer, ForeignKey("profissionais.id"), nullable=False)

    # Atalhos para acessar os objetos ligados
    paciente = relationship("Paciente")
    profissional = relationship("Profissional")