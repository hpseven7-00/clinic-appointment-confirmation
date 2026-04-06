"""
Colunas da planilha de agendamentos:
S: vamos usar
N: não vamos usar

Índice

Unidade
Sala
Sol. Interno
Sol. Externo
Idade
Como conheceu
ID Amigo
Cod. Legado
CPF
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
Cód. Atendimento - S - sessao
Agendado em - S - sessao
Agendado por - S - sessao
Confirmado em - S - sessao
Confirmado por - S - sessao
Data do Agendamento - S - sessao
Hora do Agendamento - S - sessao
Profissional - S - profissional
Paciente - S - paciente
Telefone - S - paciente


"""

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://clinic_user:clinic1234@localhost:5432/clinic"
)

conn = engine.connect()
print("Conectado!")