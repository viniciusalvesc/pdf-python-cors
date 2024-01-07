from pusher import Pusher
import os

class PusherService:
    def __init__(self):
        self.pusher = Pusher(
            app_id=os.getenv('PUSHER_APP_ID'),
            key=os.getenv('PUSHER_KEY'),
            secret=os.getenv('PUSHER_SECRET'),
            cluster=os.getenv('PUSHER_CLUSTER'),
            ssl=True,
        )

    def send_trigger(self, channel, event, data):
        print(channel, event, data)
        self.pusher.trigger(channel, event, data)