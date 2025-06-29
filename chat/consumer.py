import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatCounsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name =  self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        
        await self.channel_layer.group_add(self.room_group_name, self.channel_name) #регистрируем текущее подключение
        await self.accept() #принимаем сокеты
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    
    async def receive(self, text_data=None):
        data = json.loads(text_data)
        message = data["message"]
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_messagea",
                "message": message       #функция отправки сообщения группе
            }
        )
    
    async def chat_message(self,event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
        }))    
        