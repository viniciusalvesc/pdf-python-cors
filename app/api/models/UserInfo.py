"""
Nome do arquivo: Users.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 09/01/2024
Descrição: Arquivo modelo da tabela user_info do banco de dados.
"""
from sqlalchemy import ForeignKey
from config.alchemy import db

class UserInfo(db.Model):
    __tablename__ = 'ft_user_info'
    
    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, ForeignKey('ft_user.id'), nullable=False, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    cpf = db.Column(db.String)
    birthdate = db.Column(db.Date)
    gender = db.Column(db.String)
    phone_number = db.Column(db.String)
    user_avatar_url = db.Column(db.String)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)

    user = db.relationship('User', back_populates='user_info')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'cpf': self.cpf,
            'birthdate': self.birthdate.isoformat() if self.birthdate else None,
            'gender': self.gender,
            'phone_number': self.phone_number,
            'user_avatar_url': self.user_avatar_url,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None,
        }