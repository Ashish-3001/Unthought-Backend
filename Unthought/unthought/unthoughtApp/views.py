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
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializers

class MemberViewSet(viewsets.ModelViewSet):
    
    queryset = Member.objects.all()
    serializer_class = MemberSerializers
    
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('User_id',)
    search_fields = ('pri_specification_submain','sec_specification_submain','unique_name')

class MemberDpViewSet(viewsets.ModelViewSet):
    
    queryset = MemberDp.objects.all()
    serializer_class = MemberDpSerializers

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
    search_fields = ('requirement1','requirement2','requirement3','requirement4')
    filter_fields = ('admin_id',)

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
    filter_fields = ('post_id','user_id')

class PostPicViewSet(viewsets.ModelViewSet):
    
    queryset = PostPic.objects.all()
    serializer_class = PostPicSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('post_id',)


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
            primary_sub_set = Post.objects.filter( Q(requirement1 = primary_sub) | Q(requirement2= primary_sub) | 
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
            print(sorted_post_id)

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
