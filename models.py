# Models of the user and health program
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# many to many join table
client_program = Table(
    'client_program',
    Base.metadata,
    Column('client_id', Integer, ForeignKey('clients.id')),
    Column('program_id', Integer, ForeignKey('programs.id')),
)

# Client details
class Client(Base):
    __tablename__ = 'clients'
    id      = Column(Integer, primary_key=True, index=True)
    name    = Column(String, nullable=False)
    age     = Column(Integer, nullable=False)
    gender  = Column(String, nullable=False)
    programs = relationship(
        "Program",
        secondary=client_program,
        back_populates="clients"
    )

# Health program details
class Program(Base):
    __tablename__ = 'programs'
    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    clients     = relationship(
        "Client",
        secondary=client_program,
        back_populates="programs"
    )
