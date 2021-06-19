from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import json
from rest_framework import filters
import django_filters.rest_framework
from django_filters import rest_framework as FilterSet
from django.db.models import Q
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import User
from .models import Member
from .models import MemberDp
from .models import Events
from .models import EventsPics
from .models import Post
from .models import SavePostMember
from .models import LikedPostMember
from .models import ProjectMember
from .models import PostPic
from .models import GroupText
from .models import IndividualChatList
from .models import IndividualText
from .models import Help
from .serializer import UserSerializers
from .serializer import MemberSerializers
from .serializer import MemberDpSerializers
from .serializer import EventsSerializers
from .serializer import EventsPicsSerializers
from .serializer import PostSerializers
from .serializer import SavePostMemberSerializers
from .serializer import LikedPostMemberSerializers
from .serializer import ProjectMemberSerializers
from .serializer import PostPicSerializers
from .serializer import LoginValidateSerializers
from .serializer import HomePostSerializers
from .serializer import PeopleInterestedSerializers
from .serializer import EventsNearMeSerializers
from .serializer import HomePostImgSerializers
from .serializer import HomeLikedAndSavedPostCheckSerializers
from .serializer import GroupTextSerializers
from .serializer import RetriveTextSerializers
from .serializer import IndividualChatListSerializers
from .serializer import IndividualTextSerializers
from .serializer import RetriveIndividualChatListSerializers
from .serializer import HelpSerializers
from .serializer import OtpCheckSerializers
import requests
import random
# Create your views here.

class UserAuthentication(ObtainAuthToken):
    def post(self, request,):
        token = ""
        serializer = self.serializer_class(data=request.data, context=(request)) 
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token.created = Token.objects.get_or_create(user=user)
        return Response(token.key)


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializers

class MemberViewSet(viewsets.ModelViewSet):
    
    queryset = Member.objects.all()
    serializer_class = MemberSerializers
    
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('User_id',)
    search_fields = ('unique_name','pri_specification_submain','sec_specification_submain','pri_specification_main','sec_specification_main',)

class MemberDpViewSet(viewsets.ModelViewSet):
    
    queryset = MemberDp.objects.all()
    serializer_class = MemberDpSerializers

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('member_id',)

class EventsViewSet(viewsets.ModelViewSet):
    
    queryset = Events.objects.all()
    serializer_class = EventsSerializers

class EventsPicsViewSet(viewsets.ModelViewSet):
    
    queryset = EventsPics.objects.all()
    serializer_class = EventsPicsSerializers

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('event_id',)

class PostsViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    search_fields = ('title_of_post','requirement1','requirement2','requirement3','requirement4',)
    filter_fields = ('admin_id','active')

class SavePostMemberViewSet(viewsets.ModelViewSet):
    
    queryset = SavePostMember.objects.all()
    serializer_class = SavePostMemberSerializers

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('post_id','member_id','saved')

class LikedPostMemberViewSet(viewsets.ModelViewSet):
    
    queryset = LikedPostMember.objects.all()
    serializer_class = LikedPostMemberSerializers

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('post_id','member_id','liked')

class ProjectMemberViewSet(viewsets.ModelViewSet):
    
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializers
    
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('post_id','user_id','active','sent',)

class PostPicViewSet(viewsets.ModelViewSet):
    
    queryset = PostPic.objects.all()
    serializer_class = PostPicSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('post_id',)

class GroupTextViewSet(viewsets.ModelViewSet):

    queryset = GroupText.objects.all()
    serializer_class = GroupTextSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('post_id','member_id',)

class IndividualChatListViewSet(viewsets.ModelViewSet):

    queryset = IndividualChatList.objects.all()
    serializer_class = IndividualChatListSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('member_id_1','member_id_2',)

class IndividualTextViewSet(viewsets.ModelViewSet):

    queryset = IndividualText.objects.all()
    serializer_class = IndividualTextSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('reciver_id','sender_id',)


class HelpViewSet(viewsets.ModelViewSet):

    queryset = Help.objects.all()
    serializer_class = HelpSerializers

class ValidatePhoneSendOTP(APIView):

    def post(self, request, *args, **kwargs):

        serializer = OtpCheckSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone']
        user_name = serializer.validated_data['user_name']
        print(phone_number)

        if phone_number and user_name:

            phone = str(phone_number)
            user = Member.objects.filter(phone_number__iexact = phone)

            if user.exists():

                return Response({
                                'status': False,
                                'detail': 'phone number is already present',
                            })
                '''key = sendotp(phone)
                if key:
                    data = LoginData.objects.filter(phone__iexact = phone)
                    if data.exists():
                        otp = str(key)
                        url = 'http://2factor.in/API/V1/99e679bc-cb75-11ea-9fa5-0200cd936042/SMS/'+phone+'/'+otp+'/EZEEJOBS'
                        r = requests.get(url)
                        if r.status_code == 200:
                            data = data.first()
                            data.data_time = datetime.now()
                            data.otp = key
                            data.save()
                            return Response({
                                'status': True,
                                'detail': 'phone number is present in both',
                                'otp': key,
                                'time': 'exists'
                            })
                        else :
                            return Response({
                                'status': True,
                                'detail': 'error in sending otp'
                            })
                    else:
                        otp = str(key)
                        url = 'http://2factor.in/API/V1/99e679bc-cb75-11ea-9fa5-0200cd936042/SMS/'+phone+'/'+otp+'/EZEEJOBS'
                        r = requests.get(url)
                        if r.status_code == 200:
                            serializer.save()
                            data = LoginData.objects.filter(phone__iexact = phone)
                            data = data.first()
                            data.data_time = datetime.now()
                            data.otp = key
                            data.save()
                            return Response({
                                'status': True,
                                'detail': 'phone number is present',
                                'otp': key
                            })
                        else:
                            return Response({
                                'status': True,
                                'detail': 'error in sending otp'
                            })
                else:
                    return Response({
                    'status': False,
                    'detail': 'Genrating otp error'
                })'''

            else :
                Username = User.objects.filter(user_name__iexact = user_name)

                if Username.exists():
                    Response({
                                'status': False,
                                'detail': 'User name is already present',
                            })

                else:
                    key = sendotp(phone)

                    if key:
                        otp = str(key)
                        url = 'http://2factor.in/API/V1/99e679bc-cb75-11ea-9fa5-0200cd936042/SMS/'+phone+'/'+otp+'/EZEEJOBS'
                        r = requests.get(url)

                        if r.status_code == 200:
                            return Response({
                            'status': True,
                            'detail': 'OTP sent',
                            'otp': key
                        })

                        else:
                            return Response({
                                'status': False,
                                'detail': 'error in sending otp'
                            })

                    else:
                        return Response({
                        'status': False,
                        'detail': 'Genrating otp error'
                    })

        else:
            return Response({
                    'status': False,
                    'detail': 'phone number or user_name not given in the post request'
                })

class LoginValidate(APIView):

    def post(self, request, *args, **kwargs):
        serializer = LoginValidateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_name = serializer.validated_data['user_name']
        password = serializer.validated_data['password']
        if user_name and password:
            user = User.objects.get(user_name = user_name)
            if user.user_name:
                correct_password = user.password
                user_id = user.pk
                user_type = user.user_type
                if password == correct_password:
                    return Response({
                        'status': True,
                        'detail': 'UserName and Pasword is present and correct',
                        'user_type': user_type,
                        'user_id': user_id
                    })
                else:
                    return Response({
                        'status': False,
                        'detail': 'UserName is present but Pasword is wronge',
                        'user_type': user_type
                    })
            else:
                return Response({
                    'status': False,
                    'detail': 'User dose not exist',
                })
        else:
            return Response({
                'status': False,
                'detail': 'Password or userName got given in post request',
            })


class HomePost(APIView):

    def post(self, request, *args, **kwargs):
        serializer = HomePostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        primary_sub = serializer.validated_data['pri_specification_submain']
        secondary_sub = serializer.validated_data['sec_specification_submain']
        primary_main = serializer.validated_data['pri_specification_main']
        secondary_main = serializer.validated_data['sec_specification_main']

        if primary_sub and secondary_sub and primary_main and secondary_main:
            primary_sub_set = Post.objects.filter( 
            Q(requirement1 = primary_sub) | Q(requirement2= primary_sub) | 
            Q(requirement3= primary_sub) | Q(requirement4= primary_sub) | 
            Q(requirement1 = secondary_sub) | Q(requirement2= secondary_sub) | 
            Q(requirement3= secondary_sub) | Q(requirement4= secondary_sub))

            primary_main_set = Post.objects.filter( Q(requirement1 = primary_main) | Q(requirement2= primary_main) | 
            Q(requirement3= primary_main) | Q(requirement4= primary_main) | 
            Q(requirement1 = secondary_main) | Q(requirement2= secondary_main) | 
            Q(requirement3= secondary_main) | Q(requirement4= secondary_main))

            compelte_sorted_set = primary_sub_set.union(primary_main_set)

            sorted_set_json = serializers.serialize('json', compelte_sorted_set)
            return HttpResponse(sorted_set_json, content_type='application/json')

        else:
            return Response({
                'status': False,
                'detail': 'correct data notgiven in post request',
            })


class TrendingProjects(APIView):

    def get(self, request, *args, **kwargs):

        trending_post  = Post.objects.all().order_by('-no_of_links')
        trending_post_limit =  trending_post[0:5]
        
        trending_post_dis = {}
        for x in trending_post_limit:
            trending_post_dis[x.id] = x.title_of_post
        print(trending_post_dis)


        return HttpResponse(trending_post_dis, content_type='application/json')

class PeopleInterested(APIView):

    def post(self, request, *args, **kwargs):
        serializer = PeopleInterestedSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        primary_sub = serializer.validated_data['pri_specification_submain']
        secondary_sub = serializer.validated_data['sec_specification_submain']

        if primary_sub and secondary_sub:
            primary_members = Member.objects.filter( Q(pri_specification_submain=primary_sub) | Q(sec_specification_submain= secondary_sub))
            secondary_members = Member.objects.filter( Q(pri_specification_submain=secondary_sub) | Q(sec_specification_submain= primary_sub))

            sorted_members = primary_members.union(secondary_members)
            
            sorted_members_json = serializers.serialize('json', sorted_members)
            return HttpResponse(sorted_members_json, content_type='application/json')

        else:
            return Response({
                'status': False,
                'detail': 'correct data notgiven in post request',
            })

class EventsNearMe(APIView):

    def post(self, request, *args, **kwargs):
        serializer = EventsNearMeSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        sort_filter = serializer.validated_data['sort_filter']
        primary_sub = serializer.validated_data['pri_specification_submain']
        secondary_sub = serializer.validated_data['sec_specification_submain']

        if sort_filter and primary_sub and secondary_sub:

            if sort_filter == 'date':

                events_data = EventsPics.objects.order_by('-date')

                events_data_json = serializers.serialize('json', events_data)
                return HttpResponse(events_data_json, content_type='application/json')

            elif sort_filter == 'rating':

                events_data = EventsPics.objects.all().order_by('-rating')

                events_data_json = serializers.serialize('json', events_data)
                return HttpResponse(events_data_json, content_type='application/json')

            elif sort_filter == 'specification':

                events_data1 = EventsPics.objects.filter( Q(categories = primary_sub) | Q(categories= secondary_sub) | Q(categories = "common") )
                events_data2 = EventsPics.objects.all()

                events_data = events_data1.union(events_data2)

                events_data_json = serializers.serialize('json', events_data)
                return HttpResponse(events_data_json, content_type='application/json')

            else:
                return Response({
                'status': False,
                'detail': 'Sort filter is wrong',
            })

        else:
            return Response({
                'status': False,
                'detail': 'correct data notgiven in post request',
            })

class HomePostImg(APIView):

    def post(self, request, *args, **kwargs):
        serializer = HomePostImgSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        sorted_post_id_char = serializer.validated_data['sorted_post_id']
        
        if sorted_post_id_char:
            sorted_post_id = sorted_post_id_char.split(',')

            my_filter_qs = Q()
            for post_id in sorted_post_id[:-1]:
                my_filter_qs = my_filter_qs | Q(post_id = post_id)
            img_data = PostPic.objects.filter(my_filter_qs)

            img_data_json = serializers.serialize('json', img_data)
            return HttpResponse(img_data_json, content_type='application/json')


        else:
            return Response({
                    'status': False,
                    'detail': 'correct data not given in post request',
                })

class HomePostMemberImg(APIView):

    def post(self, request, *args, **kwargs):
        serializer = HomePostImgSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        sorted_member_id_char = serializer.validated_data['sorted_post_id']
        
        if sorted_member_id_char:
            sorted_member_id = sorted_member_id_char.split(',')

            my_filter_qs = Q()
            for member_id in sorted_member_id[:-1]:
                my_filter_qs = my_filter_qs | Q(member_id = member_id)
            img_data = MemberDp.objects.filter(my_filter_qs)

            img_data_json = serializers.serialize('json', img_data)
            return HttpResponse(img_data_json, content_type='application/json')


        else:
            return Response({
                    'status': False,
                    'detail': 'correct data not given in post request',
                })

class SavedPost(APIView):

    def post(self, request, *args, **kwargs):
        serializer = HomePostImgSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        sorted_post_id_char = serializer.validated_data['sorted_post_id']
        
        if sorted_post_id_char:
            sorted_post_id = sorted_post_id_char.split(',')

            my_filter_qs = Q()
            for post_id in sorted_post_id[:-1]:
                my_filter_qs = my_filter_qs | Q(id = post_id)
            data = Post.objects.filter(my_filter_qs)

            data_json = serializers.serialize('json', data)
            return HttpResponse(data_json, content_type='application/json')


        else:
            return Response({
                    'status': False,
                    'detail': 'correct data not given in post request',
                })

class PostMemberRequest(APIView):

    def post(self, request, *args, **kwargs):
        serializer = HomePostImgSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        sorted_post_id_char = serializer.validated_data['sorted_post_id']
        
        if sorted_post_id_char:
            sorted_post_id = sorted_post_id_char.split(',')

            my_filter_qs = Q()
            for post_id in sorted_post_id[:-1]:
                my_filter_qs = my_filter_qs | Q(post_id = post_id)
            post_data = ProjectMember.objects.filter(my_filter_qs)

            post_data_filter = post_data.filter(active = False)
            post_data_filter_json = serializers.serialize('json', post_data_filter)
            return HttpResponse(post_data_filter_json, content_type='application/json')


        else:
            return Response({
                    'status': False,
                    'detail': 'correct data not given in post request',
                })

class Members(APIView):

    def post(self, request, *args, **kwargs):
        serializer = HomePostImgSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        sorted_member_id_char = serializer.validated_data['sorted_post_id']
        
        if sorted_member_id_char:
            sorted_member_id = sorted_member_id_char.split(',')

            my_filter_qs = Q()
            for member_id in sorted_member_id[:-1]:
                my_filter_qs = my_filter_qs | Q(id = member_id)
            data = Member.objects.filter(my_filter_qs)

            data_json = serializers.serialize('json', data)
            return HttpResponse(data_json, content_type='application/json')


        else:
            return Response({
                    'status': False,
                    'detail': 'correct data not given in post request',
                })


class HomeLikedAndSavedPostCheck(APIView):

    def post(self, request, *args, **kwargs):
        serializer = HomeLikedAndSavedPostCheckSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_id = serializer.validated_data['post_id']
        member_id = serializer.validated_data['member_id']
        action = serializer.validated_data['action']
        
        if post_id and member_id and action:
            if action == 'liked' or action == 'disliked':
                try: 
                    item_l = LikedPostMember.objects.get( member_id = member_id , post_id = post_id)
                    if action == 'liked':
                        LikedPostMember.objects.filter(pk = item_l.pk).update(liked= True)
                        return Response({
                            'detail': 'not_first',
                        })
                    else:
                        LikedPostMember.objects.filter(pk = item_l.pk).update(liked= False)
                        return Response({
                            'detail': 'not_first',
                        })
                except:
                    return Response({
                            'detail': 'first',
                        })
            elif action == 'saved' or action == 'unsaved':
                try: 
                    item = SavePostMember.objects.get( member_id = member_id , post_id = post_id)
                    if action == 'saved':
                        SavePostMember.objects.filter(pk = item.pk).update(saved= True)
                        return Response({
                            'detail': 'not_first',
                        })
                    else:
                        SavePostMember.objects.filter(pk = item.pk).update(saved= False)
                        return Response({
                            'detail': 'not_first',
                        })
                except:
                    return Response({
                            'detail': 'first',
                        })
            else:
                return Response({
                    'detail': 'invalid action given in post request',
                })
        else:
            return Response({
                    'detail': 'correct data not given in post request',
                }) 

class RetriveChats(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RetriveTextSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        item_id = serializer.validated_data['item_id']
        reciver_id = serializer.validated_data['reciver_id']
        type = serializer.validated_data['type']
        limit = serializer.validated_data['limit']
        start_limit = serializer.validated_data['start_limit']
        if item_id and type and limit:
            if type == 'group':
                texts = GroupText.objects.filter(post_id_id = item_id).order_by('-createdAt')[start_limit:limit]
                texts_json = json.dumps([{'member_name': o.member_name, 'createdAt': o.createdAt, 'message': o.message} for o in texts],cls=DjangoJSONEncoder)
                return HttpResponse(texts_json, content_type='application/json')

            elif type == 'personal':
                print(item_id, reciver_id)
                texts = IndividualText.objects.filter(sender_id_id = item_id, reciver_id_id = reciver_id).order_by('-createdAt')[start_limit:limit]
                print(texts)
                texts_json = json.dumps([{'sender_name': o.sender_name, 'createdAt': o.createdAt, 'message': o.message} for o in texts],cls=DjangoJSONEncoder)
                print(texts_json)
                return HttpResponse(texts_json, content_type='application/json')

            else :
                return Response({
                    'detail': 'correct type not given in post request',
                })            
            
        else:
             return Response({
                    'detail': 'correct data not given in post request',
                })
     
class RetriveIndividualChatList(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RetriveIndividualChatListSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        member_id = serializer.validated_data['member_id']

        if member_id:
            member_list = IndividualChatList.objects.filter( Q(member_id_1 = member_id) | Q(member_id_2 = member_id)).order_by('-last_message_date')
            
            member_list_json = serializers.serialize('json', member_list)

            return HttpResponse(member_list_json, content_type='application/json')

        else:
            return Response({
                    'detail': 'correct data not given in post request',
                })

class DeleteEmptyChats(APIView):

    def get(self, request, *args, **kwargs):

        IndividualChatList.objects.filter(last_message = '/?#$%^&*(!@#$^?').delete()

        return Response({
                    'detail': 'Completed Deleting Empty Chats',
                })

def sendotp(phone):
    if phone:
        key = random.randint(999, 9999)
        return key
    else: 
        return False
