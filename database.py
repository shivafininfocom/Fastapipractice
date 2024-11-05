from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/beta"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Initialize the database
def init_db():
    SQLModel.metadata.create_all(engine)

# Dependency to get the DB session
def get_session():
    with Session(engine) as session:
        yield session

