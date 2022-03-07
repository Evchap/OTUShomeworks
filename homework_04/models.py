import os
from datetime import datetime
import asyncio
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    ForeignKey,
)

from sqlalchemy.orm import (
    declarative_base,
    scoped_session,
    # async_scoped_session,
    sessionmaker,
    relationship,
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:postgres@localhost/postgres"
DB_URL = "sqlite:///homework-04.db"

async def inittables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


engine = create_async_engine(PG_CONN_URI, echo=True,)

Base = declarative_base(bind=engine)
session_factory = sessionmaker(bind=engine, class_=AsyncSession)
Session = scoped_session(session_factory)



class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    username = Column(String(32), nullable=False)
    email = Column(String(32), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"{self.__class__.__name__}(" \
               f"id={self.id}, " \
               f"name={self.name!r}, " \
               f"username={self.username!r}, " \
               f"email={self.email!r}, " \
               f"created_at={self.created_at!r})"

    def __repr__(self):
        return str(self)

    posts = relationship("Post", back_populates="user")
#    posts = relationship("Post", backref="user")

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    title = Column(Text, nullable=False, default="", server_default="")
    body = Column(String, nullable=False, default="", server_default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"{self.__class__.__name__}(" \
               f"id={self.id}, " \
               f"user_id={self.id}, " \
               f"name={self.title!r}, " \
               f"body={self.username!r}, " \
               f"created_at={self.created_at!r})"

    def __repr__(self):
        return str(self)

    user = relationship("User", back_populates="posts")

def create_tables():
    Base.metadata.create_all()

def create_user(name: str, username: str, email: str)-> User:

    session = Session()

    user = User(name=name, username = username, email=email)
    print("created", user)

    session.add(user)
    session.commit()
    print("saved", user)
    session.close()
    return user


# async def main():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)


# if __name__ == "__main__":
#     main()

