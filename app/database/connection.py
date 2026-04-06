"""
Colunas da planilha de agendamentos:
S: vamos usar
N: não vamos usar

Cód. Atendimento - S
Índice
Agendado em - S
Agendado por - S
Confirmado em - S
Confirmado por - S
Data do Agendamento - S
Hora do Agendamento - S
Unidade
Sala
Profissional - S
Sol. Interno
Sol. Externo
Paciente - S
Idade
Como conheceu
ID Amigo
Cod. Legado
CPF
Telefone - S
E-mail
Matrícula
Tipo de Atendimento
Tipo do Item
Qtd. Item
Item
Status do Agendamento
Forma de Pagamento
Tipo de Guia
Acomodação

"""

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://clinic_user:clinic1234@localhost:5432/clinic"
)

conn = engine.connect()
print("Conectado!")