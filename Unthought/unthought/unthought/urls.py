"""unthought URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from unthoughtApp import views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()

router.register(r'User',views.UserViewSet)
router.register(r'Member',views.MemberViewSet)
router.register(r'MemberDp',views.MemberDpViewSet)
router.register(r'Events',views.EventsViewSet)
router.register(r'EventsPics',views.EventsPicsViewSet)
router.register(r'Post',views.PostsViewSet)
router.register(r'SavePostMember',views.SavePostMemberViewSet)
router.register(r'LikedPostMember',views.LikedPostMemberViewSet)
router.register(r'ProjectMember',views.ProjectMemberViewSet)
router.register(r'PostPic',views.PostPicViewSet)
router.register(r'GroupChat',views.GroupTextViewSet)
router.register(r'IndividualChatList',views.IndividualChatListViewSet)
router.register(r'IndividualText',views.IndividualTextViewSet)
router.register(r'Help',views.HelpViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('validate-otp/', views.ValidatePhoneSendOTP.as_view()),
    path('validate-user/', views.LoginValidate.as_view()),
    path('sorted-posts/', views.HomePost.as_view()),
    path('post-members/', views.PostMemberRequest.as_view()),
    path('members/', views.Members.as_view()),
    path('sorted-posts-img/', views.HomePostImg.as_view()),
    path('saved-posts/', views.SavedPost.as_view()),
    path('sorted-posts-liked/', views.HomeLikedAndSavedPostCheck.as_view()),
    path('sorted-people-img/', views.HomePostMemberImg.as_view()),
    path('People_interested/', views.PeopleInterested.as_view()),
    path('Trending_post/', views.TrendingProjects.as_view()),
    path('events_near_you/', views.EventsNearMe.as_view()),
    path('get_texts/', views.RetriveChats.as_view()),
    path('empty_chat_delete/', views.DeleteEmptyChats.as_view()),
    path('individual_chat_list/', views.RetriveIndividualChatList.as_view()),
    path('chat/', include('active_zone.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
