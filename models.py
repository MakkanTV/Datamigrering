from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ssn = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False)
    accounts = relationship("Account", back_populates="customer")

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    balance = Column(Numeric, default=0, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship("Customer", back_populates="accounts")








