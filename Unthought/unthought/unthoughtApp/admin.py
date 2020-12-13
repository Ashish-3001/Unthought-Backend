from django.contrib import admin
from .models import User
from .models import Member
from .models import SavePostMember
from .models import LikedPostMember
from .models import MemberDp
from .models import Events
from .models import EventsPics
from .models import Post
from .models import ProjectMember
from .models import PostPic

# Register your models here.
admin.site.register(User)
admin.site.register(Member)
admin.site.register(SavePostMember)
admin.site.register(LikedPostMember)
admin.site.register(MemberDp)
admin.site.register(Events)
admin.site.register(EventsPics)
admin.site.register(Post)
admin.site.register(ProjectMember)
admin.site.register(PostPic)
