"""
Nome do arquivo: pusherService.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo do serviço Pusher, responsável por enviar mensagens em tempo real.
"""
from pusher import Pusher
from decouple import config

class PusherService:
    def __init__(self):
        self.pusher = Pusher(
            app_id=config('PUSHER_APP_ID'),
            key=config('PUSHER_KEY'),
            secret=config('PUSHER_SECRET'),
            cluster=config('PUSHER_CLUSTER'),
            ssl=True,
        )

    def send_trigger(self, channel, event, data):
        print(channel, event, data)
        self.pusher.trigger(channel, event, data)