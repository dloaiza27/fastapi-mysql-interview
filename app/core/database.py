from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Nota: El candidato debe parametrizar estas variables de entorno
DATABASE_URL = "mysql+pymysql://root:root@db:3306/interview"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_db_connection():
    """
    Nota: Se espera que el candidato haga un SELECT real
    para comprobar la conexión con la base de datos.
    """
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except:
        return False
