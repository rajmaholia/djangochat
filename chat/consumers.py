from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async 
import json 

from django.contrib.auth.models import User

from .models import Room , Message 

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['id']
        self.room_group_name = f'chat_{self.room_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self,code):
        print(f'Code : {code}')
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self,text_data):
        data = json.loads(text_data)
        username = data['username']
        message =  data['message']
        room_id = data['roomid']

        await self.save_message(username,room_id,message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_messages',
                'username':username,
                'message':message,
                'room_id':room_id
            }
        )
    
    async def chat_messages(self,event):
        message = event['message']
        username = event['username']
        room_id = event['room_id']

        await self.send(text_data=json.dumps({
            'message':message,
            'username':username,
            'room_id':room_id
            }))
    
    @sync_to_async
    def save_message(self,username,room,message):
        user = User.objects.get(username=username)
        room = Room.objects.get(id=room)

        Message.objects.create(sender=user,room=room,content=message)