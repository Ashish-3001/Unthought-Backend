from django.shortcuts import render
from rest_framework import viewsets
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
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializers

class MemberViewSet(viewsets.ModelViewSet):
    
    queryset = Member.objects.all()
    serializer_class = MemberSerializers

class MemberDpViewSet(viewsets.ModelViewSet):
    
    queryset = MemberDp.objects.all()
    serializer_class = MemberDpSerializers

class EventsViewSet(viewsets.ModelViewSet):
    
    queryset = Events.objects.all()
    serializer_class = EventsSerializers

class EventsPicsViewSet(viewsets.ModelViewSet):
    
    queryset = EventsPics.objects.all()
    serializer_class = EventsPicsSerializers

class PostsViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class SavePostMemberViewSet(viewsets.ModelViewSet):
    
    queryset = SavePostMember.objects.all()
    serializer_class = SavePostMemberSerializers

class LikedPostMemberViewSet(viewsets.ModelViewSet):
    
    queryset = LikedPostMember.objects.all()
    serializer_class = LikedPostMemberSerializers

class ProjectMemberViewSet(viewsets.ModelViewSet):
    
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializers

class PostPicViewSet(viewsets.ModelViewSet):
    
    queryset = PostPic.objects.all()
    serializer_class = PostPicSerializers
