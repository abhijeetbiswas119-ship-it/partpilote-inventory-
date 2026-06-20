from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Supabase Transaction Pooler URL
DATABASE_URL = "postgresql://postgres.yqeetslsbvfmqipdoccu:Abhijeet%4028@aws-1-ap-northeast-1.pooler.supabase.com:6543/postgres"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"sslmode": "require"}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()