import json
from channels.generic.websocket import AsyncWebsocketConsumer
 
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name,
        )
        await self.accept()
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName ,
            self.channel_layer,
        )
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message ,
                "username" : username ,
            },)
    async def sendMessage(self , event) :
        message = event["message"]
        username = event["username"]
        await self.send(text_data = json.dumps({"message":message ,"username":username}))

# import json
# from channels.generic.websocket import JsonWebsocketConsumer


# class ChatConsumer(JsonWebsocketConsumer):
#     """
#     This consumer is used to show user's online status,
#     and send notifications.
#     """

#     def __init__(self, *args, **kwargs):
#         super().__init__(args, kwargs)
#         self.room_name = None

#     def connect(self):
#         print("Connected!")
#         self.room_name = "home"
#         self.accept()
#         self.send_json(
#             {
#                 "type": "welcome_message",
#                 "message": "Hey there! You've successfully connected!",
#             }
#         )

#     def disconnect(self, code):
#         print("Disconnected!")
#         return super().disconnect(code)

#     def receive_json(self, content, **kwargs):
#         print(content)
#         return super().receive_json(content, **kwargs)
