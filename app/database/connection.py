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

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL não definida. Verifique seu .env")

# Cria engine
engine = create_engine(
    DATABASE_URL,
    echo=True,          # log das queries (tira em produção)
    pool_pre_ping=True  # evita conexões mortas
)

# Cria fábrica de sessões
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Função pra pegar sessão (padrão)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Teste opcional de conexão
def test_connection():
    try:
        with engine.connect() as conn:
            print("Banco conectado com sucesso.")
    except Exception as e:
        print("Erro ao conectar no banco:", e)