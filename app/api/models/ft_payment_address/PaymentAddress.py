"""
Nome do arquivo: PaymentAddress.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 16/01/2024
Descrição: Arquivo modelo da tabela ft_payment_address do banco de dados.
"""
from sqlalchemy import ForeignKey, Column, String, Date
from sqlalchemy.orm import relationship
from app.db.sqlalchemy import Base

class PaymentAddress(Base):
    __tablename__ = 'ft_payment_address'

    id = Column(String(36), primary_key=True)
    user_id = Column(String, ForeignKey('ft_user.id'), nullable=False, unique=True)
    zip_code = Column(String)
    country = Column(String)
    state = Column(Date)
    city = Column(String)
    neighborhood = Column(String)
    street = Column(String)
    number = Column(String)
    complement = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    deleted_at = Column(Date)

    user = relationship('User', back_populates='payment_address')
    payment_history = relationship('PaymentHistory', back_populates='payment_address')