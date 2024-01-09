"""
Nome do arquivo: Users.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 09/01/2024
Descrição: Arquivo modelo da tabela personalInfo do banco de dados.
"""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from config.alchemy import db

class PersonalInfo(db.Model):
    __tablename__ = 'personalInfo'
    
    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, ForeignKey('users.id'), nullable=False, unique=True)
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

    user = relationship('User', backref='user_profile')