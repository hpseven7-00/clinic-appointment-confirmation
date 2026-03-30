from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://clinc_user:clinic1234@45.230.236.166:5432/clinic"
)

conn = engine.connect()
print("Conectado!")