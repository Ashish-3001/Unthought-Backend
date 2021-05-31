import json
from os import truncate
import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from channels.db import database_sync_to_async
from unthoughtApp.models import GroupText
from unthoughtApp.models import IndividualText
from unthoughtApp.models import IndividualChatList

class ChatRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print(self.room_group_name)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        try:
            status = text_data_json['status']
            my_id = text_data_json['my_id']
            message3 = text_data_json['message']
            connect_id = text_data_json['connect_id']
            print(text_data_json)
            
            await updatelastseen(my_id,message3,connect_id,status)
            return

        except:
            try:
                post_id = text_data_json['post_id']
                member_id = text_data_json['member_id']
                member_name = text_data_json['member_name']
                message1 = text_data_json['message']    

                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chatroom_message',
                        'post_id': post_id,
                        'member_id': member_id,
                        'member_name': member_name,
                        'message': message1,
                    }
                )
            except:
                reciver_id = text_data_json['reciver_id']
                sender_id = text_data_json['sender_id']
                sender_name = text_data_json['sender_name']
                message2 = text_data_json['message']

                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'personal_message',
                        'reciver_id': reciver_id,
                        'sender_id': sender_id,
                        'sender_name': sender_name,
                        'message': message2,
                    }
                )

        '''if text_data_json['post_id']:
            post_id = text_data_json['post_id']
            member_id = text_data_json['member_id']
            member_name = text_data_json['member_name']
            message1 = text_data_json['message']    

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chatroom_message',
                    'post_id': post_id,
                    'member_id': member_id,
                    'member_name': member_name,
                    'message': message1,
                }
            )
        elif text_data_json['reciver_id']:
            reciver_id = text_data_json['reciver_id']
            sender_id = text_data_json['sender_id']
            sender_name = text_data_json['sender_name']
            message2 = text_data_json['message']

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'personal_message',
                    'reciver_id': reciver_id,
                    'sender_id': sender_id,
                    'sender_name': sender_name,
                    'message': message2,
                }
            )
        
        elif text_data_json['status']:
            print(text_data_json)
            return'''


    async def chatroom_message(self, event):

        post_id = int(event['post_id'])
        member_id = event['member_id']
        member_name = event['member_name']
        message = event['message']    

        text = await savetext(post_id,member_id,member_name,message)

        await self.send(text_data=json.dumps({
            'member_name': text.member_name, 
            'message': text.message,
            'createdAt': text.createdAt,
        },
        cls=DjangoJSONEncoder ))


    async def personal_message(self, event):
        
        reciver_id = event['reciver_id']
        sender_id = event['sender_id']
        sender_name = event['sender_name']
        message = event['message']

        text = await savetextpersonal(reciver_id,sender_id,sender_name,message)

        await self.send(text_data=json.dumps({
            'sender_name': text.sender_name, 
            'message': text.message,
            'createdAt': text.createdAt,
        },
        cls=DjangoJSONEncoder ))

    pass

@database_sync_to_async
def savetext(post_id,member_id,member_name,message):
    text = GroupText(post_id_id = post_id, member_id_id = member_id, member_name = member_name, message = message )
    text.save()
    return text

@database_sync_to_async
def savetextpersonal(reciver_id,sender_id,sender_name,message):
    text = IndividualText(reciver_id_id = reciver_id, sender_id_id = sender_id, sender_name = sender_name, message = message)
    text.save()
    return text

@database_sync_to_async
def updatelastseen(my_id,message,connect_id,status):
    
    if status == True:
        print("hello")
        item = IndividualChatList.objects.get(pk = int(connect_id))
        IndividualChatList.objects.filter(pk = item.pk).update(last_message = message)
        IndividualChatList.objects.filter(pk = item.pk).update(last_message_date = datetime.datetime.now() )
        if item.member_id_1 == my_id:
            IndividualChatList.objects.filter(pk = item.pk).update(member_1_seen = True)
        else:
            IndividualChatList.objects.filter(pk = item.pk).update(member_2_seen = True)
    elif status == False:
        item = IndividualChatList.objects.get(pk = int(connect_id))
        if item.member_id_1 == my_id:
            IndividualChatList.objects.filter(pk = item.pk).update(member_1_seen = True)
        else:
            IndividualChatList.objects.filter(pk = item.pk).update(member_2_seen = True)
    else: 
        pass
    return