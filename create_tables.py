from app.database.connection import engine
from app.models.base import Base

from app.models.paciente import Paciente
from app.models.profissional import Profissional
from app.models.sessao import Sessao

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso (ou já existiam).")