# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from .models import Message
# from django.contrib.auth.models import User

# class ChatConsumer(AsyncWebsocketConsumer):
#        async def connect(self):
#            self.room_name = self.scope['url_route']['kwargs']['room_name']
#            self.room_group_name = f'chat_{self.room_name}'

#            await self.channel_layer.group_add(
#                self.room_group_name,
#                self.channel_name
#            )
#            await self.accept()

#        async def disconnect(self, close_code):
#            await self.channel_layer.group_discard(
#                self.room_group_name,
#                self.channel_name
#            )

#        async def receive(self, text_data):
#            data = json.loads(text_data)
#            message = data['message']
#            sender = self.scope['user']
#            receiver_username = self.room_name
#            receiver = User.objects.get(username = receiver_username)

#            Message.objects.create(
#                 sender=sender,
#                 receiver=receiver,
#                 content = message
#            )

#            await self.channel_layer.group_send(
#                self.room_group_name,
#                {
#                    'type': 'chat_message',
#                    'message': message,
#                    'sender': sender.username,
#                }
#            )

#        async def chat_message(self, event):
#            message = event['message']
#            sender = event['sender']

#            await self.send(text_data=json.dumps({
#                 'message': message,
#                 'sender' : sender,
#                 }))

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        print(f"WebSocket connected: {self.room_group_name}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(f"WebSocket disconnected: {self.room_group_name}")

    async def receive(self, text_data):
        print("Data received:", text_data)
        data = json.loads(text_data)
        message = data['message']
        sender = self.scope['user']
        receiver_username = self.room_name

        try:
            receiver = User.objects.get(username=receiver_username)
            # Save the message to the database
            Message.objects.create(
                sender=sender,
                receiver=receiver,
                content=message
            )
            print("Message saved to the database:", message)

            # Broadcast the message to the WebSocket group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender': sender.username,
                }
            )
        except User.DoesNotExist:
            print(f"Error: User '{receiver_username}' does not exist")

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))
        print(f"Message sent to WebSocket: {message}")
