"""
Nome do arquivo: initialize.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 13/01/2024
Descrição: Arquivo responsável pela instância principal do APIRouter.
"""
from fastapi import APIRouter
from app.api.routers.users import users
from app.api.routers.auth import auth

router = APIRouter()

router.include_router(auth.auth_router)
router.include_router(users.users_router)
