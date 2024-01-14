"""
Nome do arquivo: UserAddress.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 11/01/2024
Descrição: Arquivo modelo da tabela ft_user_address do banco de dados.
"""
from sqlalchemy import ForeignKey, Column, String, Date
from sqlalchemy.orm import relationship
from app.db.sqlalchemy import Base

class UserAddress(Base):
    __tablename__ = 'ft_user_address'

    id = Column(String(36), primary_key=True)
    user_id = Column(String, ForeignKey('ft_user.id'), nullable=False, unique=True)
    zipcode = Column(String)
    country = Column(String)
    state = Column(String)
    city = Column(String)
    neighborhood = Column(String)
    street = Column(String)
    number = Column(String)
    complement = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    deleted_at = Column(Date)

    user = relationship('User', back_populates='user_address')
