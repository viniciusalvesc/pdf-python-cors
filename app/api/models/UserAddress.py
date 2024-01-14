"""
Nome do arquivo: Users.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 11/01/2024
Descrição: Arquivo modelo da tabela user_address do banco de dados.
"""
from sqlalchemy import ForeignKey
from config.alchemy import db

class UserAddress(db.Model):
    __tablename__ = 'ft_user_address'

    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String, ForeignKey('ft_user.id'), nullable=False, unique=True)
    zipcode = db.Column(db.String)
    country = db.Column(db.String)
    state = db.Column(db.String)
    city = db.Column(db.String)
    neighborhood = db.Column(db.String)
    street = db.Column(db.String)
    number = db.Column(db.String)
    complement = db.Column(db.String)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)

    user = db.relationship('User', back_populates='user_address')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'zipcode': self.zipcode,
            'country': self.country,
            'state': self.state,
            'city': self.city,
            'neighborhood': self.neighborhood,
            'street': self.street,
            'number': self.number,
            'complement': self.complement,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None,
        }