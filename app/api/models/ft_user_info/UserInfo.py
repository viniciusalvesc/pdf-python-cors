"""
Nome do arquivo: UserInfo.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 09/01/2024
Descrição: Arquivo modelo da tabela user_info do banco de dados.
"""
from sqlalchemy import ForeignKey, Column, String, Date
from sqlalchemy.orm import relationship
from app.db.sqlalchemy import Base

class UserInfo(Base):
    __tablename__ = 'ft_user_info'
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('ft_user.id'), nullable=False, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    cpf = Column(String)
    birthdate = Column(Date)
    gender = Column(String)
    phone_number = Column(String)
    user_avatar_url = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    deleted_at = Column(Date)

    user = relationship('User', back_populates='user_info')
