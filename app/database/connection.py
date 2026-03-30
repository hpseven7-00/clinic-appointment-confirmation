from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://clinic_user:clinic1234@localhost:5432/clinic"
)

conn = engine.connect()
print("Conectado!")