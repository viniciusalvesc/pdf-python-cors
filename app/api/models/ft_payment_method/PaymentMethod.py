"""
Nome do arquivo: PaymentMethod.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 16/01/2024
Descrição: Arquivo modelo da tabela ft_payment_method do banco de dados.
"""
from sqlalchemy import ForeignKey, Column, String, Date
from sqlalchemy.orm import relationship
from app.db.sqlalchemy import Base

class PaymentMethod(Base):
    __tablename__ = 'ft_payment_method'

    id = Column(String(36), primary_key=True)
    user_id = Column(String, ForeignKey('ft_user.id'), nullable=False, unique=True)
    name = Column(String)
    card_number = Column(String)
    expiration_date = Column(Date)
    cvv = Column(String)
    status = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    deleted_at = Column(Date)

    user = relationship('User', back_populates='payment_method')
    payment_history = relationship('PaymentHistory', back_populates='payment_method', uselist=True)
    