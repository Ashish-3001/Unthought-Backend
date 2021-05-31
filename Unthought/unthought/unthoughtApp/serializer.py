from django.db import models
from django.db.models import fields
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
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id',
        'user_name',
        'password',
        'user_type',
        'user_login_date')

class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
        'id',
        'unique_name',
        'User_id',
        'Member_name',
        'gender',
        'dob',
        'phone_number',
        'email',
        'working_status',
        'company_name',
        'college_name',
        'course',
        'pri_specification_main',
        'pri_specification_submain',
        'sec_specification_main',
        'sec_specification_submain',
        'desc',
        'no_of_post',
        'no_of_groups')

class MemberDpSerializers(serializers.ModelSerializer):
    class Meta:
        model = MemberDp
        fields = (
        'id',
        'member_id',
        'member_dp')

class EventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = (
        'id',
        'event_name',
        'mode',
        'date',
        'time',
        'venue',
        'categories',
        'contact_no',
        'email',
        'website',
        'desc',
        'rating')

class EventsPicsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EventsPics
        fields = (
        'id',
        'event_id',
        'event_name',
        'event_mode',
        'rating',
        'date',
        'categories',
        'event_dp',
        'event_pic1',
        'event_pic2')

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
        'id',
        'admin_id',
        'admin_name',
        'admin_designation',
        'title_of_post',
        'short_desc',
        'long_desc',
        'requirement1',
        'requirement2',
        'requirement3',
        'requirement4',
        'goal_of_project',
        'workdone',
        'progress_status',
        'no_of_links',
        'no_of_saved',
        'active')

class SavePostMemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = SavePostMember
        fields = (
        'id',
        'member_id',
        'member_name',
        'post_id',
        'post_title',
        'saved')

class LikedPostMemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = LikedPostMember
        fields = (
        'id',
        'member_id',
        'member_name',
        'post_id',
        'post_title',
        'liked')

class ProjectMemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = (
        'id',
        'post_id',
        'post_title',
        'user_id',
        'user_name',
        'user_type',
        'active')

class PostPicSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostPic
        fields = (
        'id',
        'post_id',
        'post_title',
        'post_dp',
        'post_pic1',
        'post_pic2',
        'active')

class LoginValidateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'user_name',
        'password')

class HomePostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
        'pri_specification_submain',
        'sec_specification_submain',
        'pri_specification_main',
        'sec_specification_main',
        )

class PeopleInterestedSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
        'pri_specification_submain',
        'sec_specification_submain',
        )

class EventsNearMeSerializers(serializers.ModelSerializer):
    sort_filter = serializers.CharField(max_length=15) 
    class Meta:
        model = Member
        fields = (
        'pri_specification_submain',
        'sec_specification_submain',
        'sort_filter',
        )

class HomePostImgSerializers(serializers.ModelSerializer):
    sorted_post_id = serializers.CharField(max_length=20)
    class Meta:
        model = Member
        fields = (
            'sorted_post_id',
        )

class HomeLikedAndSavedPostCheckSerializers(serializers.ModelSerializer):
    post_id = serializers.IntegerField()
    member_id = serializers.IntegerField()
    action = serializers.CharField(max_length=20)
    class Meta:
        model = Post
        fields = (
            'post_id',
            'member_id',
            'action',
        )

class GroupTextSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupText
        fields = (
            'id',
            'post_id',
            'member_id',
            'member_name',
            'createdAt',
            'message'
        )


class RetriveTextSerializers(serializers.ModelSerializer):
    item_id = serializers.IntegerField()
    reciver_id = serializers.IntegerField()
    type = serializers.CharField(max_length=10)
    limit = serializers.IntegerField()
    start_limit = serializers.IntegerField()
    class Meta:
        model = GroupText
        fields = (
            'item_id',
            'reciver_id',
            'type',
            'limit',
            'start_limit'
        )

class IndividualChatListSerializers(serializers.ModelSerializer):
    class Meta:
        model = IndividualChatList
        fields = (
            'id',
            'member_id_1',
            'member_name_1',
            'member_id_2',
            'member_name_2',
            'last_message',
            'member_1_seen',
            'member_2_seen',
            'last_message_date'
        )

class IndividualTextSerializers(serializers.ModelSerializer):
    class Meta:
        model = IndividualText
        fields = (
            'id',
            'reciver_id',
            'sender_id',
            'sender_name',
            'createdAt',
            'message'
        )

class RetriveIndividualChatListSerializers(serializers.ModelSerializer):
    member_id = serializers.IntegerField()
    class Meta:
        model = IndividualChatList
        fields = (
            'member_id',
        )


class HelpSerializers(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ( 
            'id',
            'user_id',
            'user_type',
            'user_name',
            'user_number',
            'user_desc',
        )