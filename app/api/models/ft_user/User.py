"""
Nome do arquivo: Users.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo modelo da tabela ft_user do banco de dados.
"""
from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship
from app.db.sqlalchemy import Base

class User(Base):
    __tablename__ = 'ft_user'

    id =  Column(String, primary_key=True)
    role = Column(String)
    email = Column(String)
    password = Column(String)
    status = Column(String)
    created_location = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    deleted_at = Column(Date)

    user_info = relationship('UserInfo', back_populates='user', uselist=True)
    user_address = relationship('UserAddress', back_populates='user', uselist=True)
    processed_item = relationship('ProcessedItem', back_populates='user', uselist=True)
