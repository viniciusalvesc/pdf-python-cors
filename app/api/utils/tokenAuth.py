"""
Nome do arquivo: tokenJWT.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 15/01/2024
Descrição: Arquivo da subclasse da HTTPBearer (fastAPI nativa), para persistir a autenticação nas rotas.
"""
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .tokenHandler import decode_jwt


class TokenAuth(HTTPBearer):
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(TokenAuth, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Schema de autenticação inválido.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Token inválido ou expirado.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Método de autenticação inválido.")

    def verify_jwt(self, jwtoken: str):
        isTokenValid = False

        try:
            payload = decode_jwt(jwtoken)
        except:
            payload = None
        
        if payload:
            isTokenValid = True
        
        return isTokenValid